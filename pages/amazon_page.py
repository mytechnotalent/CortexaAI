# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import csv

from pages.speak import Speak
from pages.page import BasePage
from pages.element import BasePageElement
from pages.locators import AmazonPageLocators


class AmazonPage(BasePage):
    """
    Child class to handle Amazon page
    """
    URL = 'https://amazon.com'

    def __init__(self, headless=True):
        """
        Attrs:
            headless: bool
        """
        super().__init__(self.URL, headless)

    @property
    def search_box(self):
        """
        Method to enter search criteria into the search box

        Returns
            object
        """
        locator = AmazonPageLocators.SEARCH_BOX
        return BasePageElement(driver=self.driver, locator=locator)

    @property
    def search_box_button(self):
        """
        Method to click the search box button

        Returns
            object
        """
        locator = AmazonPageLocators.SEARCH_BOX_BUTTON
        return BasePageElement(self.driver, locator=locator)

    def scrape(self):
        """
        Method to scrape
        """
        speak = Speak()
        items = self.driver.find_elements_by_xpath(AmazonPageLocators.ITEMS)
        try:
            with open('items.csv', 'a') as csvfile:
                item_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                for item in range(len(items)):
                    print(items[item].text)
                    item_writer.writerow([items[item].text, 39.90])
                    speak.speech(items[item].text)
        except AssertionError:
            pass
