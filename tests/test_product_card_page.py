import allure
from page_object.product_card_page import ProductPage


@allure.feature('Product page')
@allure.story('Check elements on product page')
def test_find_element_on_product_card(browser):
    product = ProductPage(browser)
    product.open(browser.url)
    product.go_to_product_card()
    product.find_button_add_to_card()
    product.find_name_product()
    product.find_rating()
    product.find_button_compare()
    product.find_link_specification()
