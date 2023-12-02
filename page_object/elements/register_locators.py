from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTER_PAGE = '/index.php?route=account/register'
    FIRSTNAME = (By.XPATH, "//*[@name='firstname']")
    LASTNAME = (By.XPATH, "//*[@name='lastname']")
    PASSWORD = (By.XPATH, "//*[@id='input-password']")
    CONFIRM_PASSWORD = (By.XPATH, "//*[@id='input-confirm']")
    EMAIL = (By.XPATH, "//*[@name='email']")
    TELEPHONE = (By.XPATH, "//*[@name='telephone']")
    CHECKBOX_AGREE_POLICY = (By.XPATH, "//*[@name='agree']")
    SUBMIT = (By.XPATH, "//*[contains(@type, 'submit')]")
    BUTTON_CONTINUE = (By.XPATH, "//*/a[.='Continue']")
    LOGOUT = (By.XPATH, "//*[@id='column-right']/*/a[.='Logout']")
