from pages.main_page import MainPage, BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

link_home = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = link_home
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser)
    page_basket.basket_validate()



# def test_guest_can_go_to_login_page(browser):
#     link = link_home
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = link_home
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_should_see_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
#
# def test_guest_should_see_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_guest_should_see_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form()
#
#
# Задание: отрицательные проверки
#
# @pytest.mark.xfail()
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = MainPage(browser, link)
#     page.open()
#     page.add_backet()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail()
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail()
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = MainPage(browser, link)
#     page.open()
#     page.add_backet()
#     page.should_not_be_success_message_is_disappeared()
