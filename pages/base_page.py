from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import allure

class BasePage:
    def __init__(self, browser: webdriver):
        self.browser: webdriver.Chrome = browser

    def find(self, args):
        return self.browser.find_element(*args)
    
    

    def is_clicable(self, args):
        element = WebDriverWait(self.browser, 20,  poll_frequency=4).until(ec.element_to_be_clickable(*args))
        print("Text is", element.text)
        return element
