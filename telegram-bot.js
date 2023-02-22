
const API_KEY = '';
const WORKER_URL = 'https://open.nemo20k.workers.dev/?link='

function extractLink(text){
  const regex = /(https:\/\/|haaretz)\S+/g;
  const matches = text.match(regex);
  return matches ? matches.pop() : undefined 
}

async function handleRequest(request) {
  console.log(request);
  console.log('start...');
  const payload = (await request.json()) ;
  const chatId = payload.message?.chat?.id;
  console.log(`id: ${chatId}`);
  const oldLink = extractLink(payload?.message?.text)
  const resultText = oldLink ? `${WORKER_URL}${oldLink}`: "no url has been found. please provide valid url"
  const response = await fetch(`https://api.telegram.org/${API_KEY}/sendMessage?chat_id=${chatId}&text=${resultText}`)
  console.log(`response: ${JSON.stringify(response)}`)
  return true;
}

export default {
  async fetch(request, env) {
    const res = await handleRequest(request);
    return new Response("success")
  }
}