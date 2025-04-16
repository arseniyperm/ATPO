import pytest
import json
import time
import math
from selenium.webdriver.common.by import By

message = ""


@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


class TestLogin:
    params = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
              "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
              "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
              "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('links', params)
    def test_authorization(self, browser, load_config, links):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        global message

        browser.get(links)
        browser.implicitly_wait(10)
        login_btn = browser.find_element(By.CSS_SELECTOR, "#ember466")
        login_btn.click()
        mail = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        mail.send_keys(login)
        passw = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        passw.send_keys(password)
        btn = browser.find_element(By.CLASS_NAME, "button_with-loader")
        btn.click()

        time.sleep(10)
        browser.implicitly_wait(10)
        field = browser.find_element(By.CLASS_NAME, "ember-text-area")
        answer = math.log(int(time.time()))
        field.send_keys(answer)
        btn = browser.find_element(By.CLASS_NAME, "submit-submission")
        btn.click()

        time.sleep(10)
        browser.implicitly_wait(10)
        feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        if feedback.text != "Correct!":
            message += feedback.text
