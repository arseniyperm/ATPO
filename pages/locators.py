from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_USERNAME = (By.ID, "#id_login-username")
    LOGIN_PASS = (By.ID, "#id_login-password")
    LOG_IN = (By.CSS_SELECTOR, "login_submit")

    REG_USERNAME = (By.ID, "#id_registration-email")
    REG_PASS = (By.ID, "#id_registration-password")
    REG_PASS_2 = (By.ID, "#id_registration-password2")
    REG = (By.CSS_SELECTOR, "registration_submit")