from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")


class AddLinkLocators():
    ADD_LINK = (By.CSS_SELECTOR, "#add_to_basket_form .btn.btn-lg.btn-primary.btn-add-to-basket")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
