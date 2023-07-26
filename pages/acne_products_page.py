from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class AcneProductsPage(Page):
    ACNE_PRODUCTS_NAMES = (By.XPATH, "//div[@class='card-wrapper']/div[@class='card-information']/"
                                     "div[@class='card-information__wrapper']/a")

    def go_to_product_details_page(self, product_name):
        acne_products = self.find_elements(*self.ACNE_PRODUCTS_NAMES)
        for product in acne_products:
            if product.text == product_name:
                product.find_element(By.XPATH, "../../../..").click()
                break
