from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        ls = [a.text for a in self.browser.find_elements(*ProductPageLocators.STRONG_TEXT_IN_MESSAGES)]
        assert product_name in ls, "Wrong product added to basket"
        assert product_price in ls, "Product`s price in basket not equal price on product page" 
