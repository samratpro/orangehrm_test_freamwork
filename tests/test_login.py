import pytest
from pages.login_page import LoginPage
from data.login_data import LoginData


class TestLogin:

    @pytest.mark.login
    def test_valid_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(LoginData.LOGIN_USER, LoginData.LOGIN_PASS)
        assert login_page.is_login_page()
    
    @pytest.mark.login
    def test_invalid_user_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("wrong", LoginData.LOGIN_PASS)
        assert login_page.is_login_page()
    
    @pytest.mark.login
    def test_invalid_pass_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(LoginData.LOGIN_USER, "wrong")
        assert login_page.is_login_page()

    @pytest.mark.login
    def test_empty_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login()
        assert login_page.is_login_page()