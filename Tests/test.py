from Pages.a_page import *
from Pages.b_page import *

class Test():
    def test_move_pages(self, driver):
        self.driver = driver

        # CREATE LP Top
        a = aPage(self.driver)
        b = a.go_to_b_page()


