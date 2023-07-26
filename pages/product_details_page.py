from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BUTTON = (By.NAME, 'add')
    IN_CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'a.product-title')
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, 'a.button--secondary')

    def add_to_cart_and_verify(self, product_name):
        # self.wait_for_element_click(*self.ADD_TO_CART_BUTTON)
        self.click(*self.ADD_TO_CART_BUTTON)
        sleep(2)
        # self.wait_for_element_appear(*self.IN_CART_PRODUCT_NAME)
        self.verify_element_text(product_name, *self.IN_CART_PRODUCT_NAME)

    def go_to_cart_page(self):
        self.click(*self.VIEW_CART_BUTTON)
