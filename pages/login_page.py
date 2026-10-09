from data.login_data import LoginData


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.login_page_url = LoginData.PAGE_URL
        self.username = page.locator(LoginData.USER_LOC)
        self.password = page.locator(LoginData.PASS_LOC)
        self.login_button = page.locator(LoginData.SUBMIT_LOC)

    def open(self):
        self.page.goto(self.login_page_url)
    
    def login(self, username='', password=''):
        if username:
            self.username.fill(username)
        if password:
            self.password.fill(password)
        self.login_button.click()
    
    # def empty_login(self):
    #     self.login_button.click()

    def is_login_page(self):
        return "/auth/login" in self.page.url