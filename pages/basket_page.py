from .locators import AddLinkBasketLocators



class BasketPage():
    def __init__(self, browser):
        self.browser = browser

    def basket_validate(self):
        basket = self.browser.find_element(*AddLinkBasketLocators.BASKET).text
        print(basket)
        assert basket == "Your basket is empty. Continue shopping", 'Ошибка корзинка не пустая'
