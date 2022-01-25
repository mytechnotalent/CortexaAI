# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """
    Class to handle main page locators
    """
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """
    Class to handle maing page search results locators
    """
    pass


class AmazonPageLocators(object):
    """
    Class to handle Amazon page locators
    """
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BOX_BUTTON = (By.ID, 'nav-search-submit-button')
    ITEMS = '//*[@id="search"]//*[@class="a-size-base-plus a-color-base a-text-normal"]'
    ITEM_WHOLE_PRICES = '//*[@id="search"]//*[@class="a-price-whole"]'
    ITEM_FRACTION_PRICES = '//*[@id="search"]//*[@class="a-price-fraction"]'
