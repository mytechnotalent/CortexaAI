# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import csv

from pages.speak import Speak
from pages.page import BasePage
from pages.element import BasePageElement
from pages.amazon_page_locators import AmazonPageLocators


class AmazonPage(BasePage):
    """
    Child class to handle Amazon page
    """
    
    def __init__(self):
        self.URL = 'https://amazon.com'
        super().__init__(self.URL)

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

    def is_results_found(self, expected_text):
        """
        Verifies that there are search results

        Params:
            expected_text: str

        Returns:
            object
        """
        return expected_text in self.driver.page_source

    def scrape(self):
        """
        Method to scrape
        """
        speak = Speak()
        items = self.driver.find_elements_by_xpath(AmazonPageLocators.ITEMS)
        items_whole_prices = self.driver.find_elements_by_xpath(AmazonPageLocators.ITEM_WHOLE_PRICES)
        items_fractional_prices = self.driver.find_elements_by_xpath(AmazonPageLocators.ITEM_FRACTION_PRICES)
        try:
            with open('items.csv', 'a') as csvfile:
                item_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                for item in range(len(items)):
                    print('{0} ${1}.{2}'.format(items[item].text, items_whole_prices[item].text, items_fractional_prices[item].text))
                    item_writer.writerow([items[item].text])
                    item_writer.writerow([items_whole_prices[item].text])
                    item_writer.writerow([items_fractional_prices[item].text])
                    speak.speech(items[item].text)
                    speak.speech(items_whole_prices[item].text)
                    speak.speech('dollars and')
                    speak.speech(items_fractional_prices[item].text)
                    speak.speech('cents')
        except AssertionError:
            pass
