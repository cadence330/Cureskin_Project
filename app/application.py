from pages.header import Header
from pages.main_page import MainPage
from pages.acne_products_page import AcneProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.acne_products_page = AcneProductsPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)


