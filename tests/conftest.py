import pytest
from pages.home.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory



@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # lp = LoginPage(driver)
    # lp.login("test@email.com", "abcabc")

    # request.cls 是当前测试所属的测试类
    # 检查当前的测试上下文是否是在类的范围内执行的
    if request.cls is not None:
        request.cls.driver = driver

    # 返回 driver
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help='Type of operating system')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')
