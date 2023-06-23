import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    def confirm_location(self):
        # Locators
        location_selector_loc = '//div[@class="_2DsdVZQ1"]'
        location_selector_moscow_loc = '//*[@id="modal-overlay"]/div/div/div[3]/div/div[1]/div[1]/a'
        # Getters
        def get_location_selector():
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, location_selector_loc)))
        def get_location_selector_moscow():
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, location_selector_moscow_loc)))
        # Methods
        def click_on_location_selector():
            get_location_selector().click()
        def click_on_location_selector_moscow():
            get_location_selector_moscow().click()
        # Actions
        click_on_location_selector()
        click_on_location_selector_moscow()
