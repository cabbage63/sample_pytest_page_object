# related page objects
from Pages.base_page import BasePage


class bPage(BasePage):
    def go_to_a_page(self):
        return aPage()

from Pages.a_page import *