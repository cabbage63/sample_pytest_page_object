# related page objects
from Pages.base_page import BasePage
from Pages.a_page import *

class bPage(BasePage):
    def go_to_b_page(self):
        return aPage(self.driver)
