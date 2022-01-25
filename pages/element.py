# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement:
    """
    Class to represent a base page element
    """
    def __init__(self, driver, locator, timeout=10):
        """
        Attrs:
            driver: object
            locator: tuple
            timeout: int, optional
        """
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.element = None
        self.find()

    def find(self):
        """
        Method to find an element
        """
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.element = element

    def input_text(self, text):
        """
        Method to input text into an element

        Params:
            text: str
        """
        self.element.send_keys(text)

    def click(self):
        """
        Method to click an element
        """
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()

    def text(self):
        """
        Method to get an element's text

        Returns
            str
        """
        text = self.element.text
        return text
