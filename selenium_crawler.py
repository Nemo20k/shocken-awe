import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROME_DRIVER_PATH = './chromedriver'

def take_screenshot(url: str, user_agent: str, save_path: str) -> str:
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

def take_pdf(url: str, user_agent: str, save_path: str) -> str:
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
