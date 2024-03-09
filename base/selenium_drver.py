import os
import time
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # 封装定位方式，根据locatorType返回对应的定位方式
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        locator_mapping = {
            'id': By.ID,
            'css': By.CSS_SELECTOR,
            'class_name': By.CLASS_NAME,
            'link_text': By.LINK_TEXT,
            'xpath': By.XPATH,
        }
        result = locator_mapping.get(locatorType, False)
        if not result:
            self.log.info(f"Locator type {locatorType} is not supported")
        return result

    # 获取元素方法，返回元素对象
    def getElement(self, locator, locatorType='css'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'{locatorType}:{locator}已发现元素')
        except:
            self.log.info(f'{locatorType}:{locator}未发现元素')
        return element

    # 获取多个元素方法，返回元素列表
    def getElementList(self, locator, locatorType='css'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f'{locatorType}:{locator} 已发现元素')
        except:
            self.log.info(f'{locatorType}:{locator} 未发现元素')
        return element

    # 点击元素方法
    def elementClick(self, locator='', locatorType='css', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'{locatorType}:{locator} 点击元素成功!')

        except:
            self.log.info(f'{locatorType}:{locator} 点击元素失败!')
            # 打印当前线程的堆栈跟踪。显示的是代码执行到当前位置的路径，生产环境可禁用
            print_stack()

    # 输入数据方法
    def sendKeys(self, data, locator='', locatorType='css', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'{locatorType}:{locator} 输入 {data} 成功!')
        except:
            self.log.error(f'{locatorType}:{locator} 输入 {data} 失败!')
            print_stack()

    # 获取文本
    def getText(self, locator='', locatorType='css', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute('innerText')
                self.log.info(f'{locatorType}:{locator} 获取文本 {text} 成功!')
            text = text.strip()
            self.log.info(f'{locatorType}:{locator} 获取文本 {text} 成功!')

        except:
            self.log.info(f'{locatorType}:{locator} 获取文本失败!')
            print_stack()

    # 检查元素是否显示
    def isElementDisplayed(self, locator='', locatorType='', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info(f'{locatorType}:{locator} 是可见的!')
            else:
                self.log.error(f'{locatorType}:{locator} 是不可见的!')
                return False

            return isDisplayed
        except:
            self.log.info('元素未找到')
            return False

    # 检查元素是否存在 - 方法1
    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info('Element Found')
                return True
            else:
                return False
        except:
            self.log.info('Element is not found')
            return False

    # 检查元素是否存在 - 方法2
    def elementPresenceCheck(self, locator, locatorType):
        try:
            elements = self.getElement(locator, locatorType)
            if len(elements) > 0:
                self.log.info('Element Found')
                return True
            else:
                self.log.info('Element is not found')
                return False
        except:
            return False

    # 获取页面标题
    def getTitle(self):
        return self.driver.title

    # 截屏
    def screenShot(self, resultMessage):
        fileName = f'{resultMessage}.{str(round(time.time() * 1000))}.png'
        # fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    # 上下滑动页面
    def webScroll(self, direction='up'):

        if direction == 'up':
            self.driver.execute_script('window.scrollBy(0, -1000);')
        elif direction == 'down':
            self.driver.execute_script('window.scrollBy(0, 700);')
        else:
            self.log.info(f'不支持 {direction} 操作，仅可 up 或 down')

    # 切换到 iframe
    def switchToFrame(self, id='', name='', index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    # 切回 主html
    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    # 获取 元素属性
    def getElementAttributeValue(self, attribute, element=None, locator='', locatorType='css'):
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)

        return value

    # 检查元素是否可用
    def isEnabled(self, locator, locatorType="id", info=""):

        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info(f"Element {info} is enabled")
            else:
                self.log.error(f"Element {info} is not enabled")
        except:
            self.log.error(f"Element {info} state could not be found")
        return enabled

    # 显示等待方法 - 通过判断元素是否可点击
    # 可拓展更多判断条件来等待
    def waitForElement(self, locator, locatorType="css",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
