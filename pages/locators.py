from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    POLE_REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    POLE_PAROL = (By.CSS_SELECTOR, "#id_registration-password1")
    POLE_DOUBLE_PAROL = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTER_TEXT = (By.CSS_SELECTOR, ".alertinner.wicon")
    SCROL_END = (By.TAG_NAME,"body")


class LoginPageLocators():
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")


class AddLinkLocators():
    ADD_LINK = (By.CSS_SELECTOR, "#add_to_basket_form .btn.btn-lg.btn-primary.btn-add-to-basket")


class AddLinkBasketLocators():
    ADD_LINK_BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    BASKET = (By.CSS_SELECTOR, "#content_inner")



class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")



