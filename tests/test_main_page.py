import pytest
import allure
from page_object.main_page import MainPage


@allure.feature('Main page')
@allure.story('Checking elements on the main page')
def test_element_of_main_page(browser):
    main = MainPage(browser)
    main.open(browser.url)
    main.find_input_field_search()
    main.find_logo_img()
    main.find_button_cart()
    main.find_first_element_in_featured()
    main.find_second_button_add_to_cart_in_featured()


@allure.feature('Main page')
@allure.story('Checking currency on the main page')
@pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
def test_currency(browser, currency):
    main = MainPage(browser)
    main.open(browser.url)
    main.currency_selection(currency)
    main.check_currency_menu(currency)
    main.check_currency_cart(currency)
