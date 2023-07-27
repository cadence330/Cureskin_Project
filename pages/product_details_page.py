from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BUTTON = (By.NAME, 'add')
    IN_CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'a.product-title')
    VIEW_CART_BUTTON = (By.ID, 'cart-icon-bubble')
    CHECK_OUT_BUTTON = (By.NAME, 'checkout')
    CONTINUE_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def add_to_cart_and_verify(self, product_name):
        self.click(*self.ADD_TO_CART_BUTTON)
        sleep(2)
        self.click(*self.VIEW_CART_BUTTON)
        sleep(2)
        self.verify_element_text(product_name, *self.IN_CART_PRODUCT_NAME)

    def go_to_cart(self):
        self.click(*self.CHECK_OUT_BUTTON)
        sleep(2)

