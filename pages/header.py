from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SHOP_BY_CONCERN_BTN = (By.XPATH, "//summary/span[@class='label']")
    ACNE_BTN = (By.CSS_SELECTOR, "a[href*='acne'] span.label")

    def go_to_acne_products(self):
        self.click(*self.SHOP_BY_CONCERN_BTN)
        sleep(2)
        # self.wait_for_element_appear(*self.ACNE_BTN)
        self.click(*self.ACNE_BTN)


