from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.XPATH, "//header/div/div/div[2]//a")
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_USERNAME = (By.ID, "#id_login-username")
    LOGIN_PASS = (By.ID, "#id_login-password")
    LOG_IN = (By.NAME, "login_submit")

    REG_USERNAME = (By.ID, "#id_registration-email")
    REG_PASS = (By.ID, "#id_registration-password")
    REG_PASS_2 = (By.ID, "#id_registration-password2")
    REG = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BTN = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    ADDED_NTF = (By.XPATH, "//div[@id='messages']/div[1]/div[1]")
