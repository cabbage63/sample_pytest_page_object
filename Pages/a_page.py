from Pages.base_page import BasePage
from Pages.b_page import *

class aPage(BasePage):
    def go_to_b_page(self):
        return bPage(self.driver)
