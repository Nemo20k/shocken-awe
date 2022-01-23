import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests


CHROME_DRIVER_PATH = './chromedriver'


def take_html(url: str, user_agent: str, save_path:str='haaretz_article.html', **kwargs) -> str:
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f'failed to connect to: {url}\nwith exception:\n', e.args)
        return
    if not save_path.endswith('.html'):
        save_path += '.html'
    with open(save_path, 'w') as f:
        f.write(response.text)
    return save_path


def take_screenshot(url: str, user_agent: str, save_path: str, **kwargs) -> str:
    options: Options = webdriver.ChromeOptions()
    options.headless = True
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))                                                                                                         
    driver.find_element_by_tag_name('body').screenshot(save_path)
    driver.quit()
    return save_path

def take_pdf(url: str, user_agent: str, save_path: str, **kwargs) -> str:
    options = webdriver.ChromeOptions()
    settings = {
        "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--kiosk-printing')
    driver = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER_PATH)
    driver.get(url)
    driver.execute_script('window.print();')
    driver.quit()
    return save_path
