from Pages.a_page import *
from Pages.b_page import *

class TestMovePages():
    def test_move_pages(self, driver):
        self.driver = driver

        # CREATE LP Top
        a = aPage()
        b = a.go_to_b_page()

        b = bPage()
        a = b.go_to_a_page()


