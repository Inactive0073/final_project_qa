from .base_page import BasePage
from .locators import CardPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def click_to_add_to_the_cart_button(self):
        product_button = self.browser.find_element(*CardPageLocators.PRODUCT_BTN)
        product_button.click()
        
    def should_be_btn_add_in_cart(self):
        assert self.is_element_present(*CardPageLocators.PRODUCT_BTN), 'The button is not present'
    
    def should_be_success_msg_about_addition(self):
        assert self.is_element_present(*CardPageLocators.PRODUCT_MSG_TITLE), 'The message about addiition to the cart is not present'
    
    def title_should_be_the_same(self):
        assert self.browser.find_element(*CardPageLocators.PRODUCT_TITLE).text == self.browser.find_element(*CardPageLocators.PRODUCT_MSG_TITLE).text
        
    def price_should_be_the_same(self):
        assert self.browser.find_element(*CardPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*CardPageLocators.PRODUCT_MSG_PRICE).text
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CardPageLocators.PRODUCT_MSG_TITLE), \
        "Success message is presented, but should not be"
        
    def should_be_disappear_message_after_addition_product_card(self):
        assert self.is_disappeared(*CardPageLocators.PRODUCT_MSG_TITLE), \
            "Success message is presented. Not disappear"