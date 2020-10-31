from Pages.base_page import BasePage

class aPage(BasePage):
    def go_to_b_page(self):
        return bPage()

from Pages.b_page import *
