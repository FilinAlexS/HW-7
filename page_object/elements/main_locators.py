from selenium.webdriver.common.by import By
from data.currency_data import CurrencyData


class MainLocators:
    FIELD_SEARCH = (By.XPATH, "//*[contains(@name, 'search')]")
    LOGO_IMG = (By.XPATH, "//*[@id='logo']//img")
    BUTTON_CART = (By.CSS_SELECTOR, ".btn-inverse")
    ALL_ELEMENTS_IN_FEATURED = (By.XPATH, "//h4/a")
    ALL_BUTTONS_ADD_TO_CART_IN_FEATURED = (By.XPATH, "//*[contains(@class, 'button-group')]/button[1]")
    CURRENCY_BUTTON = (By.XPATH, "//*[.='Currency']/..")

    currency_mapper = {
        "EUR": {
            "active_currency_list": CurrencyData.EUR_ACTIVE,
            "currency_in_cart": CurrencyData.EUR_CART
        },
        "USD": {
            "active_currency_list": CurrencyData.USD_ACTIVE,
            "currency_in_cart": CurrencyData.USD_CART
        },
        "GBP": {
            "active_currency_list": CurrencyData.GBP_ACTIVE,
            "currency_in_cart": CurrencyData.GBP_CART
        }
    }
