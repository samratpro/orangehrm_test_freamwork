from data.time_data import TimeData
from data.login_data import LoginData
from pages.time_page import TimePage
from pages.login_page import LoginPage

import pytest

class TestTime:

    def login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(LoginData.LOGIN_USER, LoginData.LOGIN_PASS)


    @pytest.mark.time
    def test_valid_employee(self, page):
        self.login(page)
        time_page = TimePage(page)
        time_page.open_time_page()
        time_page.search_emp_name(TimeData.emp_name)


        


