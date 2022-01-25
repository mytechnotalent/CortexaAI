# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import unittest
from selenium import webdriver

from pages import page


class PythonOrgSearch(unittest.TestCase):
    """
    A sample test class to show how page object works
    """
    URL = 'http://python.org'

    def setUp(self):
        """
        Method to handle test setup
        """
        self.driver = webdriver.Chrome('/Users/developer/PycharmProjects/af/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver.get(self.URL)

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """
        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
