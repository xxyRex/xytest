import pytest
from pages.courses.register_courses_page import RegisterCoursesPage


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestsRegisterCourses:

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.rcp.enterCourseName('java')
        self.rcp.selectCourseToEnroll()
        self.rcp.clickEnrollButton()
        self.rcp.webScroll('down')
        self.rcp.enterCreditCardInformation('123123', '1212', '1231231232')
        self.rcp.clickEnrollSubmitButton()
        result = self.rcp.verifyEnrollFailed()
        assert result is True
