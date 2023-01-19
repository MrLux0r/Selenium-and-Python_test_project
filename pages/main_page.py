from .base_page import BasePage
from .locators import ProductPageLocators, AddLinkLocators



class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def add_backet(self):
        product_add_backet = self.browser.find_element(*AddLinkLocators.ADD_LINK)
        product_add_backet.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
