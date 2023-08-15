import time
import random
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
#
# firefox_driver_path = GeckoDriverManager().install()
# browser_service = Service(executable_path=firefox_driver_path)
# browser = webdriver.Firefox(service=browser_service)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.chrome}")

chrome_driver_path = ChromeDriverManager().install()
browser_service = Service(excutable_path=chrome_driver_path)
browser = webdriver.Chrome(service=browser_service, options=options)

url = 'https://passport.yandex.ru/auth/'

try:
    browser.get(url=url)
    time.sleep(5)

    email_input = browser.find_element(By.ID, "passp-field-login")
    email_input.clear()
    email_input.send_keys("yv-test")
    time.sleep(5)

    # browser.refresh()
    # browser.save_screenshot('p_yangex.png')
    # time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()


