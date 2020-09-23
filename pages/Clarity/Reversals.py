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

"""This class have all web elements of Clarity Reversals Grid"""

class Reversals(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.reversal_grid_click = "//a[@href='/Clarity/Reversals']"
        self.reversal_grid_page = "//td[@class='Text NPI NPI_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"
        self.error = "//h2[contains(text(),' Sorry, an error occurred while processing your request.')]"


    """Verify Reversals Screen"""
    def reversals_grid(self):
        self.waitForElement(self.reversal_grid_click).click()
        # self.waitForElement(self.defaultview).click()
        error = len(self.driver.find_elements_by_xpath(self.error))
        if error > 0:
            self.screenShot("Reversals Screen Error")
            self.driver.back()
            return False
        else:
            self.waitForData(self.reversal_grid_page)
            return True
