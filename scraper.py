import time
import selenium.webdriver as  webdriver
from selenium.webdriver.chrome.service import Service


def scrap_website(website: str): 
    print("Launch webbrowser")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source()
        time.sleep(1)
        print(html[0:100])
        return html
    finally:
        driver.quit()


