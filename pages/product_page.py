from .base_page import BasePage
from .locators import AddLinkLocators



class Page_Object(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*AddLinkLocators.ADD_LINK), "Not button add backet"
        link = self.browser.find_element(*AddLinkLocators.ADD_LINK)
        link.click()
        self.solve_quiz_and_get_code()

