import time
import allure
from page_object.base_page import BasePage
from page_object.elements.admin_locators import AdminLocators


class AdminPage(BasePage):
    PATH = AdminLocators.ADMIN_PAGE

    def open(self, url):
        self._open(url, self.PATH)

    @allure.step
    def find_input_field_username(self):
        self.element(AdminLocators.FIELD_USERNAME)

    @allure.step
    def find_input_field_password(self):
        self.element(AdminLocators.FIELD_PASSWORD)

    @allure.step
    def find_text_opencart_in_footer(self):
        self.element(AdminLocators.TEXT_OPENCART_IN_FOOTER)

    @allure.step
    def find_button_login(self):
        self.element(AdminLocators.BUTTON_LOGIN)

    @allure.step
    def check_text_in_cardheader(self):
        self.verify_text_in_element(AdminLocators.TEXT_IN_CARDHEADER, AdminLocators.TEXT_IN_CARD_HEADER)

    @allure.step
    def input_username(self, text):
        self.logger.info("<====    Start Logining in admin page    ====>")
        self._input(self.element(AdminLocators.FIELD_USERNAME), text)

    @allure.step
    def input_password(self, text):
        self._input(self.element(AdminLocators.FIELD_PASSWORD), text)

    @allure.step("Click login button")
    def submit_login(self):
        self.click(self.element(AdminLocators.BUTTON_LOGIN))
        self.logger.info("<====    Finish Logining in admin page    ====>")

    @allure.step("Check userpic is visible")
    def userpic_is_visible(self):
        time.sleep(1)
        return self.is_visible_element(AdminLocators.USERPIC)

    def login_to_admin(self):
        self.input_username('user')
        self.input_password('bitnami')
        self.submit_login()
