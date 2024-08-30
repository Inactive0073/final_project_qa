from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH, '//a[contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_BTN_PROCEED = (By.XPATH, '//a[contains(@href, "checkout")]')
    BASKET_CONTINUE_LINK = (By.XPATH, '//div[@id="content_inner"]/p/a')


class LoginPageLocators:
    LOGIN_NAME = (By.CSS_SELECTOR, "#id_login-username")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.XPATH, '//form[@id="register_form"]/button[@data-loading-text]')


class CardPageLocators:
    PRODUCT_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_MSG_TITLE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    PRODUCT_MSG_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) div strong")
