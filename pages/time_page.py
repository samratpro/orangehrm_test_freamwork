from data.time_data import TimeLocator


class TimePage:

    def __init__(self, page):
        self.page = page

    
    def open_time_page(self):
        self.page.locator(TimeLocator.time_locator).click()
    
    def search_emp_name(self, employee_name):
        input_ele = self.page.locator(TimeLocator.input_locator)
        input_ele.press_sequentially(employee_name, delay=500)
        
        select_ele = self.page.locator(TimeLocator.select_emp_locator)
        select_ele.wait_for(state="visible", timeout=10000)
        select_ele.click()

        self.page.wait_for_timeout(10000)

    def check_view(self):
        self.page.locator(TimeLocator.view_locator).click()
    
    def create_time(self):
        self.page.locator(TimeLocator.create_time_locator).click()
    
    def submit(self):
        self.page.locator(TimeLocator.submit_button).click()



