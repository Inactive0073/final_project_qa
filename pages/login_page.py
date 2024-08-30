from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.expected_conditions import url_contains
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert url_contains('login'), 'The URL doesn`t contain a login.'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_NAME), 'The login form isn`t present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), 'The registration form isn`t present'
        
    def register_new_user(self):
        f = faker.Faker()
        
        email = f.email(True,'fakelandia.fake')
        password = f.password(9)
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
    