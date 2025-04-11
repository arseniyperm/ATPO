from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = int(a.text)
    b = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = int(b.text)
    b += a

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(b))
    #select.select_by_index(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
