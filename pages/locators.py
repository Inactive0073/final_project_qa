from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_NAME = (By.CSS_SELECTOR, '#id_login-username')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    
class CardPageLocators:
    PRODUCT_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_MSG_TITLE = (By.CSS_SELECTOR, '#messages div:nth-child(1) div strong')
    PRODUCT_MSG_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) div strong')