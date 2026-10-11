from data.myinfo_data import InfoData
from data.login_data import LoginData
from pages.myinfo_page import MyInfo
from pages.login_page import LoginPage
import pytest

class TestMyinfo:


    def login(self, page):
        page = LoginPage(page)
        page.open()
        page.login(LoginData.LOGIN_USER, LoginData.LOGIN_PASS)

    @pytest.mark.myinfo
    def test_myinfo_valid(self, page):
        self.login(page)
        my_info_page = MyInfo(page)
        my_info_page.perform_action(InfoData.name)



        
