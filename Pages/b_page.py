# related page objects
from Pages.base_page import BasePage

class bPage(BasePage):
    def go_to_a_page(self):
        return aPage(self.driver)

# move import page object to the end of module
# http://effbot.org/zone/import-confusion.html
from Pages.a_page import *