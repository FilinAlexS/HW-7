import time
import allure
from page_object.base_page import BasePage
from page_object.elements.main_locators import MainLocators
from data.currency_data import select_currency


class MainPage(BasePage):

    def open(self, url):
        self._open(url)

    @allure.step
    def find_input_field_search(self):
        self.element(MainLocators.FIELD_SEARCH)

    @allure.step
    def find_logo_img(self):
        self.element(MainLocators.LOGO_IMG)

    @allure.step
    def find_button_cart(self):
        self.element(MainLocators.BUTTON_CART)

    @allure.step
    def find_first_element_in_featured(self):
        list_featured = self.elements(MainLocators.ALL_ELEMENTS_IN_FEATURED)
        return list_featured[0]

    @allure.step
    def find_second_button_add_to_cart_in_featured(self):
        return self.elements(MainLocators.ALL_BUTTONS_ADD_TO_CART_IN_FEATURED)[1]

    @allure.step("Currency selection {text}")
    def currency_selection(self, text):
        self.click(self.element(MainLocators.CURRENCY_BUTTON))
        self.click(self.element(select_currency(text)))

    @allure.step
    def check_currency_menu(self, currency):
        time.sleep(0.5)
        self.is_visible_element(MainLocators.currency_mapper.get(currency).get("active_currency_list"))

    @allure.step
    def check_currency_cart(self, currency):
        self.is_visible_element(MainLocators.currency_mapper.get(currency).get("currency_in_cart"))
