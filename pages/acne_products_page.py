from pages.base_page import Page
from selenium.webdriver.common.by import By


class AcneProductsPage(Page):
    ACNE_PRODUCTS = (By.XPATH, "//ul[@id='product-grid']/li")

    def go_to_product_details_page(self, product_name):
        acne_products = self.find_elements(*self.ACNE_PRODUCTS)
        acne_products[2].click()
        # or
        # self.find_element(By.LINK_TEXT, product_name).click()



