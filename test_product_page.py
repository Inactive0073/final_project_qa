from .pages.product_page import ProductPage
import pytest

xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [f'{mask}{i}' for i in range(10) if i != xfile]
xlink = pytest.param(f'{mask}{xfile}', marks=pytest.mark.xfail(reason=f"mistake on page {mask}{xfile}"))
links.insert(xfile, xlink)

@pytest.mark.test_any_value_in_offer
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_btn_add_in_cart()
    product_page.click_to_add_to_the_cart_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_msg_about_addition()
    product_page.title_should_be_the_same()
    product_page.price_should_be_the_same()

@pytest.mark.xfail
@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_to_add_to_the_cart_button()
    product_page.should_not_be_success_message()

@pytest.mark.smoke
def test_guest_cant_see_success_message(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_to_add_to_the_cart_button()
    product_page.should_be_disappear_message_after_addition_product_card()
    

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()