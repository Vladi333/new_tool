from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.LINK_TEXT, "Click")
result_selector = (By.ID, "result-text")


class LikeAButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/button/like_a_button")

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def button_click(self):
        try:
            self.is_clicable(button_selector)
        except Exception:
            print("Button Is not clicable")
        self.button().click()


    def result(self):
        return self.find(result_selector)

    def result_text(self):
        return self.result().text
