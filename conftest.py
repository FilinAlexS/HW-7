import pytest
import logging
import datetime
import allure
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, SafariOptions

EXECUTOR = 'localhost'
URL = 'https://demo.opencart.com'  # 'http://192.168.1.7', 'https://demo.opencart.com', http://192.168.1.2:8888


def pytest_addoption(parser):
    parser.addoption("--browser", default="safari")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default=EXECUTOR)
    parser.addoption("--url", action="store", default=URL)
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    CMD_EXECUTOR = f'http://{executor}:4444/wd/hub'

    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Remote(
            command_executor=CMD_EXECUTOR,
            options=options
        )
    elif browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Remote(
            command_executor=CMD_EXECUTOR,
            options=options
        )
    elif browser_name == "safari":
        options = SafariOptions()
        driver = webdriver.Remote(
            command_executor=CMD_EXECUTOR,
            options=options
        )
    else:
        raise ValueError(f'Driver {browser_name} not supported.')

    if maximize:
        driver.maximize_window()

    driver.url = url
    driver.logger = logger
    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    with allure.step("Browser %s started" % browser_name):
        return driver
