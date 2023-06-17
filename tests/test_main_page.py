import time
from pages.main_page import Main_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_buy_product():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    main_page = Main_page(driver)
    #driver.get('https://www.florist.ru/')
    #driver.maximize_window()
    #time.sleep(10)
    main_page.open_main_page()