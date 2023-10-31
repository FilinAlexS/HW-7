from selenium.webdriver.common.by import By


class CurrencyData:
    EUR_CART = (By.XPATH, "//*[contains(text(), '0 item(s) - 0.00€')]")
    EUR_ACTIVE = (By.XPATH, "//strong[contains(text(),'€')]")
    EUR = (By.XPATH, "//*/form//li/*[text()='€ Euro']")

    USD_CART = (By.XPATH, "//*[contains(text(),'0 item(s) - $0.00')]")
    USD_ACTIVE = (By.XPATH, "//strong[contains(text(),'$')]")
    USD = (By.XPATH, "//*/form//li/*[text()='$ US Dollar']")

    GBP_CART = (By.XPATH, "//*[contains(text(),'0 item(s) - £0.00')]")
    GBP_ACTIVE = (By.XPATH, "//strong[contains(text(),'£')]")
    GBP = (By.XPATH, "//*/form//li/*[text()='£ Pound Sterling']")


def select_currency(currency):
    if currency == "EUR":
        return CurrencyData.EUR
    elif currency == "USD":
        return CurrencyData.USD
    elif currency == "GBP":
        return CurrencyData.GBP
    else:
        raise ValueError(f'Currency {currency} not supported.')
