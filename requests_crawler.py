import requests

def take_html(url: str, user_agent: str, save_path:str='haaretz_article.html') -> str:
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f'failed to connect to: {url}\nwith exception:\n', e.args)
        return
    with open(save_path, 'w') as f:
        f.write(response.text)
    return save_path