import pytest
from utils import env as utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'headless':
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_window_size(1600, 700)

    if browser == 'ie':
        driver = webdriver.Ie()
        # capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
        # capabilities['acceptSslCerts'] = True
        # driver = webdriver.Ie(capabilities=capabilities)

    if browser == 'chrome':
        # driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(options=options)

    if browser == 'edge':
        options = EdgeOptions()
        options.use_chromium = True
        driver = Edge(options=options)

    elif browser == 'firefox':
        driver = webdriver.Firefox()

        # driver.set_window_position(920, 0)

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(utils.baseURL)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()




