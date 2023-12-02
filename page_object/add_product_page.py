import time
import allure
from selenium.webdriver.common.by import By
from data.iphone_15 import Iphone15
from page_object.admin_page import AdminPage
from page_object.elements.product_locators import AddProductLocators


class AddProductPage(AdminPage):

    @allure.step("Go to products in catalog")
    def go_to_products_in_catalog(self):
        self.click(self.element(AddProductLocators.MENU_CATALOG))
        self.click(self.element(AddProductLocators.MENU_PRODUCT))

    @allure.step("Click button add new in products")
    def click_button_add_new_in_products(self):
        self.logger.info("<====    Start create new product    ====>")
        self.click(self.element(AddProductLocators.ADD_NEW))

    @allure.step("Input product name {text}")
    def input_product_name(self, text):
        self._input(self.element(AddProductLocators.PRODUCT_NAME), text)

    @allure.step("Input description")
    def input_description(self, text):
        self._input(self.element(AddProductLocators.DESCRIPTION), text)

    @allure.step("Input meta tag")
    def input_meta_tag(self, text):
        self._input(self.element(AddProductLocators.META_TAG), text)

    @allure.step("Go to Data tab")
    def go_to_data_tab(self):
        self.click(self.element(AddProductLocators.DATA_TAB))

    @allure.step("Input model")
    def input_model(self, text):
        self._input(self.element(AddProductLocators.MODEL), text)

    @allure.step("Input price")
    def input_price(self, text):
        self._input(self.element(AddProductLocators.PRICE), text)

    @allure.step("Input quantity")
    def input_quantity(self, text):
        self._input(self.element(AddProductLocators.QUANTITY), text)

    @allure.step("Go to Links tab")
    def go_to_links_tab(self):
        self.click(self.element(AddProductLocators.LINKS_TAB))

    @allure.step("Input manufacturer")
    def input_manufacturer(self, text):
        self._input(self.element(AddProductLocators.MANUFACTURER), text)
        time.sleep(0.5)
        self.click(self.element((By.XPATH, f'//a[.="{text}"]')))

    @allure.step("Input category")
    def input_category(self, text):
        self._input(self.element(AddProductLocators.CATEGORY), text)
        time.sleep(0.5)
        self.click(self.element((By.XPATH, f'//a[.="{text}"]')))

    @allure.step("Go to SEO tab")
    def go_to_seo_tab(self):
        self.click(self.element(AddProductLocators.SEO_TAB))

    @allure.step("Input SEO")
    def input_seo(self, text):
        self._input(self.element(AddProductLocators.SEO), text)

    @allure.step("Go to Image tab")
    def go_to_image_tab(self):
        self.click(self.element(AddProductLocators.IMAGE_TAB))

    @allure.step("Change default image")
    def change_default_image(self):
        self.click(self.element(AddProductLocators.IMAGE))
        self.click(self.element(AddProductLocators.BUTTON_EDIT_IMAGE))
        self.click(self.element(AddProductLocators.DIRECTORY))
        time.sleep(1)
        self.click(self.elements(AddProductLocators.DIRECTORY)[2])
        self.click(self.element(AddProductLocators.IMAGE_IPHONE))

    @allure.step("Click Save button")
    def save_change(self):
        self.click(self.element(AddProductLocators.SAVE))
        self.logger.info("<====    Finish create new product    ====>")

    def _find_product_by_name(self, text):
        return (By.XPATH, f"//*[@class='text-left'][.='{text}']")

    @allure.step("Check add new product by name")
    def check_add_new_product(self, text):
        return self.is_visible_element(self._find_product_by_name(text))

    @allure.step("Click Delete button")
    def _click_button_delete(self):
        self.click(self.element(AddProductLocators.BUTTON_DELETE))

    def delete_product_by_name(self, text):
        with allure.step(f"Find product by name and click on checkbox"):
            self.logger.info("<====    Start Delete new product '%s'    ====>" % str(text))
            self.click(
                self.element((By.XPATH, f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input")))
        self._click_button_delete()
        with allure.step(f"Switch to alert and accept"):
            self.driver.switch_to.alert.accept()
        self.logger.info("<====    Finish Delete new product    ====>")

    @allure.step("Check absence new product by name")
    def check_absence_new_product(self, text):
        time.sleep(2)
        item = self.driver.find_elements(By.XPATH,
                                         f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input")
        self.logger.info("%s: Verify absence new product '%s'." % (self.class_name, str(text)))
        a = []
        return 1 if item == a else 0

    def create_a_product(self):
        self.go_to_products_in_catalog()
        time.sleep(1)
        self.click_button_add_new_in_products()
        self.input_product_name(Iphone15.PRODUCT_NAME)
        self.input_description(Iphone15.DESCRIPTION)
        self.input_meta_tag(Iphone15.META_TAG)
        self.go_to_data_tab()
        self.input_model(Iphone15.MODEL)
        self.input_price(Iphone15.PRICE)
        self.input_quantity(Iphone15.QUANTITY)
        self.go_to_links_tab()
        self.input_manufacturer(Iphone15.MANUFACTURER)
        self.input_category(Iphone15.CATEGORY)
        self.go_to_seo_tab()
        self.input_seo(Iphone15.SEO)
        self.go_to_image_tab()
        self.change_default_image()
