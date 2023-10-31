from selenium.webdriver.common.by import By


class AdminLocators:
    ADMIN_PAGE = '/admin'
    FIELD_USERNAME = (By.XPATH, "//*[@name='username']")
    FIELD_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    TEXT_OPENCART_IN_FOOTER = (By.XPATH, "//*[text()='OpenCart']")
    BUTTON_LOGIN = (By.XPATH, "//*[contains(@type, 'submit')]")
    TEXT_IN_CARDHEADER = (
        By.XPATH, "//*[contains(@class, 'fa-lock') and ../text()=' Please enter your login details.']/..")
    TEXT_IN_CARD_HEADER = "Please enter your login details."
    USERPIC = (By.XPATH, '//img[@id="user-profile"]')
