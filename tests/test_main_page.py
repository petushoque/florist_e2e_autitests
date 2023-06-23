import time
from pages.main_page import Main_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_buy_product():
    s = Service(ChromeDriverManager().install())
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(service=s, desired_capabilities=caps, options=options)
    main_page = Main_page(driver)
    main_page.open_main_page()