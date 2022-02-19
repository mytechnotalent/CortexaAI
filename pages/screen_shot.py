# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import os
import time
import datetime


class Screenshot:
    """
    Class to handle screenshot functionality
    """
    
    def __init__(self):
        self.dt_format = '%Y%m%d_%H%M%S'
        self.cdt = datetime.datetime.fromtimestamp(time.time()).strftime(self.dt_format)
        self.current_location = os.getcwd()
        self.img_folder = self.current_location + '/images/'
        if not os.path.exists(self.img_folder):
            os.mkdir(self.img_folder)
        self.pic = self.img_folder + self.cdt + '.png'

    def capture(self, driver):
        """
        Method to capture a screenshot during test automation
        """
        driver.save_screenshot(self.pic)
