import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke  # pytest - s - v - m smoke test_3_4_fixtures.py
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    @pytest.mark.regression # @pytest.mark.skip
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

    @pytest.mark.xfail(reason="fixing this bug right now")  # метка - ожидаемо падающий тест
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

    @pytest.mark.parametrize('language', ["ru", "en-gb"])   # Параметр и список значений
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
