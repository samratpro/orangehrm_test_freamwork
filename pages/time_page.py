from data.time_data import TimeLocator


class TimePage:

    def __init__(self, page):
        self.page = page

    
    def open_time_page(self):
        self.page.locator(TimeLocator.time_locator).click()
    
    def search_emp_name(self, employee_name):
        self.page.locator(TimeLocator.input_locator).type(employee_name, delay=500)

        self.page.locator(TimeLocator.select_emp_locator).wait_for(state="visible")
        self.page.locator(TimeLocator.select_emp_locator).click()

        self.page.wait_for_timeout(10000)

    def check_view(self):
        self.page.locator(TimeLocator.view_locator).click()
    
    def create_time(self):
        self.page.locator(TimeLocator.create_time_locator).click()
    
    def submit(self):
        self.page.locator(TimeLocator.submit_button).click()



