import pytest
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestsLogin:

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginSuccessful()
        assert result1 == 'https://www.letskodeit.com/'

        result2 = self.lp.verifyTitle()
        if not result2:
            self.lp.screenShot('Title Verification')

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login()
        result = self.lp.verifyLoginFailed()

        assert result is True
