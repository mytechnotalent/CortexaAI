# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from subprocess import Popen, PIPE
from selenium import webdriver


class BasePage:
    """
    Base class to initialize the base page that will be called from all pages
    """
    
    def __init__(self, url):
        """
        Params:
            url: str
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )
        self.driver.get(url)

    def run_cmds(self, cmds):
        """
        Method to run a list of shell commands in one shell

        Params:
            cmds: list

        Returns:
            tuple
        """
        shell_cmd = ' && '.join(cmds)
        proc = Popen(shell_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()
        stdout_results = stdout.decode().splitlines()
        stderr_results = stderr.decode().splitlines()
        return stdout_results, stderr_results

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
