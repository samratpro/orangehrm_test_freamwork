from data.myinfo_data import InfoLocator

class MyInfo:

    def __init__(self, page):
        self.page = page
        self.info_tab_loc = InfoLocator.my_info_tab_loc
        self.name_loc = InfoLocator.my_name_loc
    
    def perform_action(self, my_name_info=''):
        self.page.click(self.info_tab_loc)
        self.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/*")
        self.page.locator(self.name_loc).clear()
        if my_name_info:
            self.page.locator(self.name_loc).type(my_name_info)
