import allure
from page_object.admin_page import AdminPage


@allure.epic('Admin page')
@allure.story('Checking elements on admin page')
def test_find_elements_on_login_admin_page(browser):
    admin = AdminPage(browser)
    admin.open(browser.url)
    admin.find_input_field_username()
    admin.find_input_field_password()
    admin.find_button_login()
    admin.find_text_opencart_in_footer()
    admin.check_text_in_cardheader()


@allure.epic('Admin page')
@allure.story('Authorization on admin page')
def test_login_admin_page(browser):
    login_admin = AdminPage(browser)
    login_admin.open(browser.url)
    login_admin.input_username("user")
    login_admin.input_password("bitnami")
    login_admin.submit_login()
    assert login_admin.userpic_is_visible()
