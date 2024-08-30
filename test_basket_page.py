import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.guest_basket
class TestBasket:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.go_to_basket_view_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_empty_basket()
        basket_page.should_be_empty_basket()
        basket_page.should_be_continue_link_if_basket_is_empty()
        basket_page.should_not_be_continue_link_if_basket()
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.go_to_basket_view_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_empty_basket()
        basket_page.should_be_empty_basket()
        basket_page.should_be_continue_link_if_basket_is_empty()
        basket_page.should_not_be_continue_link_if_basket()