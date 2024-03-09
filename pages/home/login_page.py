import time

from base.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        # 继承父类 __init__
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "https://www.letskodeit.com/login"
    _email_field = "#email.form-control.input-md"
    _password_field = "#login-password"
    _login_button = "button#login"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email='', password=''):
        # self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # 验证登陆成功
    def verifyLoginSuccessful(self):
        time.sleep(3)
        result = self.driver.current_url

        return result

    # 验证登陆失败
    def verifyLoginFailed(self):
        time.sleep(1)
        result = self.isElementPresent(self._login_button, 'css')

        return result

    # 验证标题
    def verifyTitle(self):
        return self.verifyPageTitle('Google')
