# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from selenium import webdriver


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """
    def __init__(self, url, headless):
        """
        Params:
            url: str
            headless: bool
        """
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url)

    def is_title_matches(self, title):
        """
        Verifies that the hardcoded text appears in page title

        Params:
            title: str
        """
        return title in self.driver.title

    def quit(self):
        """
        Destroy chromedriver instance
        """
        self.driver.quit()
