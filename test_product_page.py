import pytest
import time
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.skip
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link1)
    page.open()
    page.add_to_basket()
    browser.implicitly_wait(5)
    page.solve_quiz_and_get_code()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.goto_basket()
    assert browser.find_element(*BasePageLocators.EMPTY_BASKET).text == "Your basket is empty. Continue shopping"


class TestUserReg:
    @pytest.fixture(autouse=True)
    def test_can_reg_new_user(browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.register_new_user(email, '123455')
        page.should_be_authorized_user()


@pytest.mark.skip
class TestUserAddToBasketFromProductPage:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.is_not_element_present(*ProductPageLocators.ADDED_NTF), \
            "Success message is presented"

    def test_guest_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        assert not page.is_not_element_present(*ProductPageLocators.ADDED_NTF), \
            "Success message is presented"

    def test_message_disappeared_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert not page.is_disappeared(*ProductPageLocators.ADDED_NTF), \
            "Success message is disappeared"

    @pytest.mark.parametrize('num', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
    def test_guest_can_add_product_to_basket(browser, num):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        browser.implicitly_wait(5)
        page.solve_quiz_and_get_code()
