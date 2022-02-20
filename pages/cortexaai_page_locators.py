# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from selenium.webdriver.common.by import By


class CortexaAIPageLocators(object):
    """
    Class to handle CortexaAI page locators
    """
    SEARCH_BOX = (By.CLASS_NAME, 'searchform')
    SEARCH_BOX_BUTTON = (By.CLASS_NAME, 'button')
    