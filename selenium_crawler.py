import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def take_screenshot(url: str, user_agent: str, save_path: str) -> str:
    options: Options = webdriver.ChromeOptions()
    options.headless = True
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
    
    driver.get(url)
    

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))                                                                                                         
    driver.find_element_by_tag_name('body').screenshot(save_path)
    driver.quit()

    return save_path