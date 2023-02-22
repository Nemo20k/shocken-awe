const USER_AGENT = 'msnbot/1.0 (+http://search.msn.com/msnbot.htm)';

/**
 * parse url and return the value of 'link' queryParam
 */
async function getLinkfromQuery(url) {
    const { searchParams } = new URL(url);
    let name = searchParams.get('link');
    return name;
}

/**
 * fetch the raw html text of a website
 * @param {*} url 
 * @returns string
 */
async function getPageContent(url) {
    try {
        const response = await fetch(url, {
            headers: {
                "User-Agent": USER_AGENT
            }
        });
        const html = await response.text();
        return html;
    } catch (error) {
        console.error(`failed to fetch ${url} with error: ${error.message}`);
    }
}

/**
 * build a Response for htmlText
 */
function buildResponse(htmlText) {
    return new Response(htmlText, {
        headers: {
            'content-type': 'text/html;charset=UTF-8',
        },
    })
}


export default {
    async fetch(request, env) {
        const link = await getLinkfromQuery(request.url);
        const html = await getPageContent(link);
        return buildResponse(html);
        // return new Response("Hello world")
    }
}