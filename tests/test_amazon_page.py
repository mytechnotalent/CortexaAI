# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import unittest

from pages.screen_shot import Screenshot
from pages.amazon_page import AmazonPage

class TestAmazonPage(unittest.TestCase):
    """
    Class to test the Amazon Page functionality
    """

    def setUp(self):
        """
        Method to handle test setup
        """
        self.amazon_page = AmazonPage()
        self.screenshot = Screenshot()

    def test_amazon_is_in_page_title(self):
        """
        Tests whether the word 'Amazon' is in the page title
        """
        # Asserts
        assert self.amazon_page.is_title_matches('Amazon'), 'Amazon title doesn\'t match.'

    def test_search_result_page_returns_results(self):
        """
        Tests if the search result page returns results
        """
        # Setup
        text = 'coffee'
        
        # Interactions
        self.amazon_page.search_box.input_text(text)
        self.amazon_page.search_box_button.click()    
        
        # Asserts
        assert self.amazon_page.is_results_found(text), 'No results found.'
        
    def tearDown(self):
        """
        Method to handle test teardown
        """
        self.screenshot.capture(self.amazon_page.driver)
        self.amazon_page.quit()


if __name__ == "__main__":
    unittest.main()
