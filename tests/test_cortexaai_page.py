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
        # asserts
        assert self.cortexaai_page.is_title_matches('CortexaAI'), 'CortexaAI title doesn\'t match.'

    def test_search_result_page_returns_results(self):
        """
        Tests if the search result page returns results
        """
        # setup
        text = 'coffee'
        # interactions
        self.cortexaai_page.search_box.input_text(text)
        self.cortexaai_page.search_box_button.click()    
        # asserts
        assert self.cortexaai_page.is_results_found(text), 'No results found.'
        
    def test_ls(self):
        """
        Tests ls
        """
        # cmds
        cmds = [
            'ls'
        ]
        stdout_results, stderr_results = self.cortexaai_page.run_cmds(cmds)
        # setup 
        actual_element_0 = stdout_results[0]
        actual_element_1 = stdout_results[1]
        actual_element_2 = stdout_results[2]
        actual_element_3 = stdout_results[3]
        actual_element_4 = stdout_results[4]
        actual_element_5 = stdout_results[5]
        actual_element_6 = stdout_results[6]
        actual_element_7 = stdout_results[7]
        actual_element_8 = stdout_results[8]
        actual_element_9 = stdout_results[9]
        actual_element_10 = stdout_results[10]
        # asserts
        self.assertTrue(stdout_results[0] == 'app', f'expected first file should be app but got "{stdout_results[0]}"')
        self.assertTrue(stdout_results[1] == 'CortexaAI.jpg', f'expected second file should be CortexaAI.jpg but got "{stdout_results[1]}"')
        self.assertTrue(stdout_results[2] == 'ctf.sh', f'expected first third should be ctf.sh but got "{stdout_results[2]}"')
        self.assertTrue(stdout_results[3] == 'docker-compose.yaml', f'expected fourth file should be docker-compose.yaml but got "{stdout_results[3]}"')
        self.assertTrue(stdout_results[4] == 'images', f'expected fifth file should be app but got "{stdout_results[4]}"')
        self.assertTrue(stdout_results[5] == 'LICENSE', f'expected sixth file should be app but got "{stdout_results[5]}"')
        self.assertTrue(stdout_results[6] == 'pages', f'expected seventh file should be app but got "{stdout_results[6]}"')
        self.assertTrue(stdout_results[7] == 'README.md', f'expected eighth file should be app but got "{stdout_results[7]}"')
        self.assertTrue(stdout_results[8] == 'requirements.txt', f'expected ninth file should be app but got "{stdout_results[8]}"')
        self.assertTrue(stdout_results[9] == 'tests', f'expected first file tenth be app but got "{stdout_results[9]}"')
        self.assertTrue(stdout_results[10] == 'venv', f'expected first file eleventh be app but got "{stdout_results[10]}"')
        
    def tearDown(self):
        """
        Method to handle test teardown
        """
        self.screenshot.capture(self.cortexaai_page.driver)
        self.cortexaai_page.quit()


if __name__ == "__main__":
    unittest.main()
