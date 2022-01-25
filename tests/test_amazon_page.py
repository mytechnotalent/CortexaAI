# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import unittest

from pages.page import BasePage
from pages.element import BasePageElement
from pages.locators import AmazonPageLocators


class TestAmazonPage(unittest.TestCase):
    """
    Class to test the Amazon Page functionality
    """
    URL = 'https://amazon.com'

    def setUp(self):
        """
        Method to handle test setup
        """
        self.main_page = BasePage(self.URL, False)

    def test_amazon_is_in_title(self):
        """
        Tests whether the word 'Amazon' is in the page title
        """
        # Asserts
        assert self.main_page.is_title_matches('Amazon'), "Amazon title doesn't match."


    def tearDown(self):
        """
        Method to handle test teardown
        """
        self.main_page.quit()


if __name__ == "__main__":
    unittest.main()
