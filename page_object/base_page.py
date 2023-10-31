import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def _open(self, url, path=''):
        with allure.step(f"Open url {url + path}"):
            self.logger.info("%s: Opening url: %s%s" % (self.class_name, url, path))
            self.driver.get(url + path)

    def click(self, locator):
        try:
            self.logger.info("%s: Click on this element" % self.class_name)
            ActionChains(self.driver).move_to_element(locator).pause(0.2).click().perform()
        except MoveTargetOutOfBoundsException:
            self.logger.info("%s: Scroll on this element" % self.class_name)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)
            self.click(locator)

    def _input(self, element, value):
        self.click(element)
        element.clear()
        self.logger.info("%s: Input value '%s'" % (self.class_name, str(value)))
        element.send_keys(value)

    def element(self, locator: tuple):
        try:
            self.logger.info("%s: Find element: %s" % (self.class_name, str(locator)))
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error("%s: Didn't wait to see the element '%s'" % (self.class_name, str(locator)))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        try:
            self.logger.info("%s: Find all elements: %s" % (self.class_name, str(locator)))
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error("%s: Didn't wait to see the elements %s" % (self.class_name, str(locator)))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def verify_product_item(self, product_name):
        self.logger.info("%s: Verify that the element %s is on the page." % (self.class_name, str(product_name)))
        return self.element((By.LINK_TEXT, product_name))

    def verify_text_in_element(self, locator: tuple, text):
        try:
            self.logger.info("%s: Verify the text in the element %s matches the expected '%s'." % (
                self.class_name, str(locator), text))
            return WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.logger.error("%s: The text in the element %s does not match the expected '%s'" % (
                self.class_name, str(locator), text))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Текст в элементе {locator} не совпадает с ожидаемым '{text}'")

    def is_visible_element(self, locator: tuple):
        visible = self.element(locator)
        self.logger.info("%s: Checks the visibility of the element %s." % (self.class_name, str(locator)))
        return visible.is_displayed()
