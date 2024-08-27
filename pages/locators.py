from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_NAME = (By.CSS_SELECTOR, '#id_login-username')
    # LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
     
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    # REG_PASSWORD1 =  (By.CSS_SELECTOR, '#id_registration-password1')
    # REG_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')