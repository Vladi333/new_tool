from selenium.webdriver.chrome.options import Options
from selenium import webdriver 
import pytest
import time
from datetime import datetime


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    return chrome_browser
