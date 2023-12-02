import allure
from page_object.register_page import RegisterPage
from data.fake_user import fake_name, fake_last_name, fake_email, fake_phone, fake_password


@allure.feature('Register page')
@allure.story('Checking elements on the registration page')
def test_element_register_page(browser):
    register = RegisterPage(browser)
    register.open(browser.url)
    register.find_input_field_firstname()
    register.find_input_field_lastname()
    register.find_input_field_email()
    register.find_input_field_password()
    register.find_checkbox_agree_policy()
    register.find_button_submit()


@allure.feature('Register page')
@allure.story('User registration on the registration page')
def test_register_user(browser):
    register = RegisterPage(browser)
    register.open(browser.url)
    register.create_user(fake_name(), fake_last_name(), fake_email(), fake_phone(), fake_password())
    assert register.check_user_login()
