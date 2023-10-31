import allure
from page_object.base_page import BasePage
from page_object.elements.register_locators import RegisterLocators


class RegisterPage(BasePage):
    PATH = RegisterLocators.REGISTER_PAGE

    def open(self, url):
        self._open(url, self.PATH)

    @allure.step
    def find_input_field_firstname(self):
        self.element(RegisterLocators.FIRSTNAME)

    @allure.step
    def input_firstname(self, text):
        self._input(self.element(RegisterLocators.FIRSTNAME), text)

    @allure.step
    def find_input_field_lastname(self):
        self.element(RegisterLocators.LASTNAME)

    @allure.step
    def input_lastname(self, text):
        self._input(self.element(RegisterLocators.LASTNAME), text)

    @allure.step
    def find_input_field_password(self):
        self.element(RegisterLocators.PASSWORD)

    @allure.step
    def input_password(self, text):
        self._input(self.element(RegisterLocators.PASSWORD), text)

    @allure.step
    def input_confirm_password(self, text):
        self._input(self.element(RegisterLocators.CONFIRM_PASSWORD), text)

    @allure.step
    def find_input_field_email(self):
        self.element(RegisterLocators.PASSWORD)

    @allure.step
    def input_email(self, text):
        self._input(self.element(RegisterLocators.EMAIL), text)

    @allure.step
    def input_telephone(self, text):
        self._input(self.element(RegisterLocators.TELEPHONE), text)

    @allure.step
    def find_checkbox_agree_policy(self):
        self.element(RegisterLocators.CHECKBOX_AGREE_POLICY)

    @allure.step
    def on_checkbox_agree_policy(self):
        self.click(self.element(RegisterLocators.CHECKBOX_AGREE_POLICY))

    @allure.step
    def find_button_submit(self):
        self.element(RegisterLocators.SUBMIT)

    @allure.step
    def click_submit(self):
        self.click(self.element(RegisterLocators.SUBMIT))

    @allure.step
    def click_continue(self):
        self.click(self.element(RegisterLocators.BUTTON_CONTINUE))

    @allure.step
    def check_user_login(self):
        return self.is_visible_element(RegisterLocators.LOGOUT)

    def create_user(self, firstname, lastname, email, tel, password):
        self.input_firstname(firstname)
        self.input_lastname(lastname)
        self.input_email(email)
        self.input_telephone(tel)
        self.input_password(password)
        self.input_confirm_password(password)
        self.on_checkbox_agree_policy()
        self.click_submit()
        self.click_continue()
