from .base_page import BasePage
from .locators import CardPageLocators

class ProductPage(BasePage):
    def click_to_add_to_the_cart_button(self):
        product_button = self.browser.find_element(*CardPageLocators.PRODUCT_BTN)
        product_button.click()
        
    def should_be_btn_add_in_cart(self):
        assert self.is_element_present(*CardPageLocators.PRODUCT_BTN), 'The button is not present'