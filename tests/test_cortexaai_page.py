# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import unittest

from pages.screen_shot import Screenshot
from pages.cortexaai_page import CortexaAIPage

class TestCortexaAIPage(unittest.TestCase):
    """
    Class to test the CortexaAI Page functionality
    """

    def setUp(self):
        """
        Method to handle test setup
        """
        self.cortexaai_page = CortexaAIPage()
        self.screenshot = Screenshot()

    def test_cortexaai_is_in_page_title(self):
        """
        Tests whether the word 'CortexaAI' is in the page title
        """
        # Asserts
        assert self.cortexaai_page.is_title_matches('CortexaAI'), 'CortexaAI title doesn\'t match.'

    def test_search_result_page_returns_results(self):
        """
        Tests if the search result page returns results
        """
        # Setup
        text = 'coffee'
        # Interactions
        self.cortexaai_page.search_box.input_text(text)
        self.cortexaai_page.search_box_button.click()    
        # Asserts
        assert self.cortexaai_page.is_results_found(text), 'No results found.'
        
    def tearDown(self):
        """
        Method to handle test teardown
        """
        self.screenshot.capture(self.cortexaai_page.driver)
        self.cortexaai_page.quit()


if __name__ == "__main__":
    unittest.main()
