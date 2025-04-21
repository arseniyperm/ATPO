from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            "URL страницы не содержит подстроку 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN), \
            "Форма логина отсутствует на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG), \
            "Форма регистрации отсутствует на странице"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REG_USERNAME)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS)
        pass1.send_keys(password)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS_2)
        pass1.send_keys(password)
        reg = self.browser.find_element(*LoginPageLocators.REG)
        reg.click()
