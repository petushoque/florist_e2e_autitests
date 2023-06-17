import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from base.base_class import Base

# class Main_page(Base):
class Main_page():

    url = 'https://www.florist.ru/'

    def __init__(self, driver):
        #super().__init__(driver)
        self.driver = driver

    # Locators
    # loc_sauce_labs_backpack_add_button = 'add-to-cart-sauce-labs-backpack'
    # loc_sauce_labs_bike_light_add_button = 'add-to-cart-sauce-labs-bike-light'
    # loc_sauce_labs_bolt_t_shirt_add_button = 'add-to-cart-sauce-labs-bolt-t-shirt'
    # loc_shopping_cart_button = 'shopping_cart_container'
    # loc_menu_button = '//button[@id="react-burger-menu-btn"]'
    # loc_about_link = '//a[@id="about_sidebar_link"]'

    # Getters
    #def get_sauce_labs_backpack_add_button(self):
    #    return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.loc_sauce_labs_backpack_add_button)))

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(10)