from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BUTTON = (By.NAME, 'add')
    # PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product__title')
    IN_CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product-content a')
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, 'a.button--secondary')

    def add_to_cart_and_verify(self, product_name):
        # self.open_url('https://shop.cureskin.com/collections/for-acne/products/sensitive-pro-cleanser')
        self.click(*self.ADD_TO_CART_BUTTON)
        sleep(2)
        # self.wait_for_element_appear(*self.IN_CART_PRODUCT_NAME)
        self.verify_element_text(product_name, *self.IN_CART_PRODUCT_NAME)

    def go_to_cart_page(self):
        self.click(*self.VIEW_CART_BUTTON)
