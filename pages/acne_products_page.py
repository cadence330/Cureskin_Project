from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class AcneProductsPage(Page):
    ACNE_PRODUCTS_NAMES = (By.CSS_SELECTOR, "div.card-wrapper a.card-information__text")

    def go_to_product_details_page(self, product_name):
        acne_products = self.find_elements(*self.ACNE_PRODUCTS_NAMES)
        for product in acne_products:
            if product.text == product_name:
                product.click()
            sleep(0.7)








