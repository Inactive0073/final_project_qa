from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    
    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BTN_PROCEED), 'Basket is not empty'
    
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BTN_PROCEED) == False, 'Basket is empty'
    
    def should_be_continue_link_if_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTINUE_LINK), 'Basket is not empty, not found continue button'
        
    def should_not_be_continue_link_if_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTINUE_LINK) == False, 'Basket is empty, not found continue button'
        