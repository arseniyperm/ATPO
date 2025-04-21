from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
