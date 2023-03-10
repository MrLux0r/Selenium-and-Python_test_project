from .base_page import BasePage
from .locators import LoginPageLocators




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"
        assert True


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present_login_form(*LoginPageLocators.FORM_LOGIN), "login form link is not presented"
        assert True


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present_register_form(*LoginPageLocators.FORM_REGISTER), "register form link is not presented"
        assert True