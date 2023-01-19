from pages.product_page import Page_Object
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




