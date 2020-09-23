import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import moment
from base.selenium_driver import SeleniumDriver
import allure
import os
from selenium import webdriver
from selenium.common.exceptions import *
from utils import env as utils
import unittest
import sys
import pytest
import utils.custom_logger as cl
import logging



class CarveOuts(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.carveouts_grid_click = "//a[@href='/Clarity/CarveOuts']"
        self.carveouts_grid_page = "//div[@class='GridWindow']//td[@class='Text Entity Entity_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

    """Verify Carve Outs Screen"""
    def carveouts_grid(self):
        self.waitForElement(self.carveouts_grid_click).click()
        result = self.waitForElement(self.carveouts_grid_page)
        time.sleep(1)
        return result




