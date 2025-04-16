import time
from selenium.webdriver.common.by import By


class TestItem:
    def test_find_add_button(self, browser):
        browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(5)

        add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert len(add_to_basket_button) > 0, "Add to basket button not found"
