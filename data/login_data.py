
class LoginData:
    LOGIN_USER = "Admin"
    LOGIN_PASS = "admin123"


class LoginLocator:
    PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USER_LOC = "//input[@placeholder='Username']"
    PASS_LOC = "//input[@placeholder='Password']"
    SUBMIT_LOC = "button[type='submit']"
