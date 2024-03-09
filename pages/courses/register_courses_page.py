import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _search_box = "input#search"
    _course = "#course-list div:nth-child(1) > div h4"
    _all_courses = "#course-list div:nth-child(1) > div h4"
    _enroll_button = "button.btn.dynamic-button"
    _cc_num = '//input[@aria-label="Credit or debit card number"]'
    _cc_exp = 'input[name="exp-date"]'
    _cc_cvv = 'input[name="cvc"]'
    _submit_enroll = "button.sp-buy"
    _enroll_error_message = "div.card-errors"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCourseToEnroll(self):
        self.elementClick(self._course)

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        self.switchToFrame(index=0)
        time.sleep(3)
        self.sendKeys(num, self._cc_num, locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(index=1)
        self.sendKeys(exp, self._cc_exp)
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(index=2)
        self.sendKeys(cvv, self._cc_cvv)
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickEnrollButton()
        self.webScroll('down')
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        element = self.waitForElement(self._enroll_error_message)
        return self.isElementDisplayed(element=element)
