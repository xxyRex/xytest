"""
@package base

实现了对整个应用程序中的所有页面都通用的方法

这个类需要被所有页面类继承


例子:
    Class LoginPage(BasePage)
"""
from base.selenium_drver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        初始化 BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        验证页面的标题

        参数:
            titleToVerify: 需要验证的页面上的标题
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
