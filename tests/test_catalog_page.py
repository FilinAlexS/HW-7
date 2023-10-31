import allure
from page_object.catalog_page import CatalogPage


@allure.feature('Catalog page')
@allure.story('Checking elements on catalog page')
def test_find_elements_on_catalog_page(browser):
    catalog = CatalogPage(browser)
    catalog.open(browser.url)
    catalog.find_icon_home()
    catalog.find_button_list_view()
    catalog.find_field_sortby()
    catalog.find_last_button_compareadd()
    catalog.check_category_cameras_in_left_menu()
