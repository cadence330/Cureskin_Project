from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.title")
    CART_PAGE_TITLE = "Your cart"

    def verify_user_on_cart_page(self):
        self.verify_element_text(*self.CART_PAGE_TITLE, *self.CART_PAGE_TITLE_LOCATOR)
