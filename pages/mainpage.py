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
    flowers_filter_loc = '//span[@class="_38kMiofv"]'

    ###
    location_popup_yes_button_loc = '//span[@class="_1Ixozll0"]'

    # Getters
    def get_flowers_filter_button(self):
        return WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, self.flowers_filter_loc)))

    ###
    def get_location_popup_yes_button(self):
        return WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, self.get_location_popup_yes_button())))

    # Methods
    def click_on_flowers_filter_button(self):
        self.get_flowers_filter_button().click()

    # Actions
    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.confirm_location()
        self.get_current_url()

        # self.click_on_flowers_filter_button()
