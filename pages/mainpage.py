import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    url = 'https://www.florist.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    flowers_filter_loc = '//div[@class="_2d6Gofi1"]'
    flowers_filter_cvety_option_loc = '//a[text()="Цветы"]'

    # Getters
    def get_flowers_filter(self):
        return WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, self.flowers_filter_loc)))
    def get_flowers_filter_cvety_option(self):
        return WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, self.flowers_filter_cvety_option_loc)))

    # Methods
    def click_on_flowers_filter(self):
        self.get_flowers_filter().click()
    def click_on_flowers_filter_cvety_option(self):
        self.get_flowers_filter_cvety_option().click()

    # Actions
    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.confirm_location()
        self.get_current_url()
        self.click_on_flowers_filter()
        self.click_on_flowers_filter_cvety_option()

