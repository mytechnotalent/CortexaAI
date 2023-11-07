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
        
    def test_expected_folders_and_files_are_in_repo(self):
        """
        Tests whether the expected folders and files are in the repo
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
        # asserts
        self.assertTrue(stdout_results[0] == 'app', f'expected file should be "app" but got "{stdout_results[0]}"')
        self.assertTrue(stdout_results[1] == 'CortexaAI.jpg', f'expected file should be "CortexaAI.jpg" but got "{stdout_results[1]}"')
        self.assertTrue(stdout_results[2] == 'docker-compose.yaml', f'expected file should be "docker-compose.yaml" but got "{stdout_results[2]}"')
        self.assertTrue(stdout_results[3] == 'images', f'expected folder should be "images" but got "{stdout_results[3]}"')
        self.assertTrue(stdout_results[4] == 'LICENSE', f'expected file should be "LICENSE" but got "{stdout_results[4]}"')
        self.assertTrue(stdout_results[5] == 'pages', f'expected folder should be "pages" but got "{stdout_results[5]}"')
        self.assertTrue(stdout_results[6] == 'README.md', f'expected file should be "README.md" but got "{stdout_results[6]}"')
        self.assertTrue(stdout_results[7] == 'requirements.txt', f'expected file should be "requirements.txt" but got "{stdout_results[7]}"')
        self.assertTrue(stdout_results[8] == 'tests', f'expected folder tenth be "tests" but got "{stdout_results[8]}"')
        self.assertTrue(stdout_results[9] == 'venv', f'expected folder eleventh be "venv" but got "{stdout_results[9]}"')

    def test_cortexaai_in_pod_name(self):
        """
        Tests if cortexaai is in the pod name
        """
        # cmds
        cmds = [
            'kubectl -n default describe pods'
        ]
        stdout_results, stderr_results = self.cortexaai_page.run_cmds(cmds)
        # setup 
        expected_substring = 'cortexaai'
        actual_element_0 = stdout_results[0]
        # asserts
        self.assertTrue(expected_substring in stdout_results[0], f'expected "{expected_substring}" in "actual_element_0" but it does not exist within "{stdout_results[0]}"')


    def tearDown(self):
        """
        Method to handle test teardown
        """
        self.screenshot.capture(self.cortexaai_page.driver)
        self.cortexaai_page.quit()


if __name__ == "__main__":
    unittest.main()
