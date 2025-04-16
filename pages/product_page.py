from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.check_name_and_price_added_product(self.get_product_name(),self.get_product_price())

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def check_name_and_price_added_product(self,name,price):
        ls = [a.text for a in self.browser.find_elements(*ProductPageLocators.STRONG_TEXT_IN_MESSAGES)]
        assert name in ls, "Wrong product added to basket"
        assert price in ls, "Product`s price in basket not equal price on product page"        