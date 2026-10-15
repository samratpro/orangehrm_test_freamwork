
class TimeData:
    emp_name = "Rahul  Das"


class TimeLocator:
    time_locator = "//a[normalize-space()='Time']"
    input_locator = "//input[@placeholder='Type for hints...']"
    select_emp_locator = "(//div[@role='listbox']//div[@role='option'][not(contains(., 'Searching'))])[1]"
    view_locator = "//button[@type='submit']"
    create_time_locator = "//button[normalize-space()='Create Timesheet']"
    submit_button = "//button[normalize-space()='Submit']"