from pages.base_page import BasePage
from pages.product_page import Page_Object
from pages.basket_page import BasketPage
import pytest

# Задание: добавление в корзину со страницы товара 4.3.2
add_backet_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# Задание: независимость от данных 4.3.3
data_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# Задание: независимость контента, ищем баг 4.3.4
@pytest.mark.parametrize('num', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    link = link
    page = Page_Object(browser, link)
    page.open()
    page.add_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser)
    page_basket.basket_validate()


class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_user()


    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_user()

