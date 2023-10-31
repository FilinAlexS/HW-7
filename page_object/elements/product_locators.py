from selenium.webdriver.common.by import By


class ProductLocators:
    PRODUCT_CARD = (By.XPATH, '//*[contains(@class, "image")]/a/img')
    BUTTON_ADD_TO_CARD = (By.XPATH, '//*[@id="button-cart"]')
    RATING = (By.XPATH, '//*[contains(@class, "rating")]')
    NAME_PRODUCT = (By.XPATH, '//*/h1')
    BUTTON_COMPARE = (By.XPATH, '//*/button[contains(@onclick, "compare.add")]')
    LINK_SPECIFICATION = (By.XPATH, '//a[.="Specification"]')


class AddProductLocators:
    MENU_CATALOG = (By.XPATH, '//*[@id="menu-catalog"]')
    MENU_PRODUCT = (By.XPATH, '//a[.="Products"]')
    ADD_NEW = (By.XPATH, '//*[contains(@class, "pull-right")]/a')
    PRODUCT_NAME = (By.ID, "input-name1")
    DESCRIPTION = (By.XPATH, '//*[@class="note-editable"]')
    META_TAG = (By.ID, "input-meta-title1")
    DATA_TAB = (By.XPATH, '//a[.="Data"]')
    MODEL = (By.ID, "input-model")
    PRICE = (By.ID, "input-price")
    QUANTITY = (By.ID, "input-quantity")
    LINKS_TAB = (By.XPATH, '//a[.="Links"]')
    MANUFACTURER = (By.ID, "input-manufacturer")
    CATEGORY = (By.ID, "input-category")
    SEO_TAB = (By.XPATH, '//a[.="SEO"]')
    SEO = (By.NAME, "product_seo_url[0][1]")
    IMAGE_TAB = (By.XPATH, '//a[.="Image"]')
    IMAGE = (By.ID, "thumb-image")
    BUTTON_EDIT_IMAGE = (By.ID, "button-image")
    DIRECTORY = (By.XPATH, "//*[@class='directory']")
    IMAGE_IPHONE = (By.XPATH, "//img[contains(@alt,'iphone.jpg')]")
    SAVE = (By.XPATH, "//button[contains(@type, 'submit')]")
    BUTTON_DELETE = (By.XPATH, '//*[@class="btn btn-danger"]')
