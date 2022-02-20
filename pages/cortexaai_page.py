# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import os

from pages.page import BasePage
from pages.element import BasePageElement
from pages.cortexaai_page_locators import CortexaAIPageLocators

class CortexaAIPage(BasePage):
    """
    Child class to handle CortexaAI page
    """
    
    def __init__(self):
        self.URL = os.getenv('URL')
        super().__init__(self.URL)

    @property
    def search_box(self):
        """
        Method to enter search criteria into the search box

        Returns
            object
        """
        locator = CortexaAIPageLocators.SEARCH_BOX
        return BasePageElement(driver=self.driver, locator=locator)

    @property
    def search_box_button(self):
        """
        Method to click the search box button

        Returns
            object
        """
        locator = CortexaAIPageLocators.SEARCH_BOX_BUTTON
        return BasePageElement(self.driver, locator=locator)

    def is_results_found(self, expected_text):
        """
        Verifies that there are search results

        Params:
            expected_text: str

        Returns:
            object
        """
        return expected_text in self.driver.page_source

