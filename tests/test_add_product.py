import allure
from page_object.add_product_page import AddProductPage
from data.iphone_15 import Iphone15


@allure.epic('Admin page')
@allure.feature('Product on admin page')
@allure.story('Add new product on admin page')
def test_add_new_product_on_admin_page(browser):
    admin = AddProductPage(browser)
    admin.open(browser.url)
    admin.login_to_admin()
    admin.create_a_product()
    admin.save_change()
    assert admin.check_add_new_product(Iphone15.PRODUCT_NAME)


@allure.epic('Admin page')
@allure.feature('Product on admin page')
@allure.story('Delete product on admin page')
def test_deleting_new_product(browser):
    admin = AddProductPage(browser)
    admin.open(browser.url)
    admin.login_to_admin()
    admin.go_to_products_in_catalog()
    admin.delete_product_by_name(Iphone15.PRODUCT_NAME)
    assert admin.check_absence_new_product(Iphone15.PRODUCT_NAME)
