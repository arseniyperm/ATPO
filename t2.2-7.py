from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/registration2.html"
    link1 = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
    input3.send_keys("@email")

    input4 = browser.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
