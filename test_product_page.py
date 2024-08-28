from .pages.product_page import ProductPage
import pytest


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_btn_add_in_cart()
    product_page.click_to_add_to_the_cart_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_msg_about_addition()
    product_page.title_should_be_the_same()
    product_page.price_should_be_the_same()