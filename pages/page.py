# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from selenium import webdriver


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """
    def __init__(self, url, headless):
        """
        Attrs:
            url: str
            headless: bool
        """
        # https://chromedriver.chromium.org/downloads
        EXECUTABLE_PATH = '/Users/developer/Downloads/CortexaAI/chromedriver'
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH, options=self.options)
        self.driver.get(url)


# class MainPage(BasePage):
#     """
#     Child class to handle page action methods
#     """
#     # Declares a variable that will contain the retrieved text
#     search_text_element = SearchTextElement()
#
#     def is_title_matches(self):
#         """
#         Method to verify that the hardcoded text "Python" appears in page title
#         """
#         return 'Python' in self.driver.title
#
#     def click_go_button(self):
#         """
#         Method to trigger a search
#         """
#         element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
#         element.click()
#
#
# class SearchResultsPage(BasePage):
#     """
#     Class to handle search results page action methods
#     """
#     def is_results_found(self):
#         """
#         Method to search for text in the page element
#
#         Returns:
#             str
#         """
#         return "No results found." not in self.driver.page_source
