#
# CortexaAI
# *********
#
# Created by My Techno Talent 03/20/21
# Modified by My Techno Talent 03/20/21
#
# Copyright: (c) 2021, My Techno Talent <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# An open-source Automation Engine that can perform full Front-End Automation, Data Science and Machine learning.
#
# required modules
# pip install gTTS
# pip install selenium
#
# Version 0.0.1 Alpha
#

from pages.speak import Speak
from pages.amazon_page import AmazonPage

if __name__ == '__main__':
    amazon_page = AmazonPage()
    speak = Speak()
    speak.speech('What would you like to search for?')
    text = input('What would you like to search for? ')
    amazon_page.search_box.input_text(text)
    amazon_page.search_box_button.click()
    amazon_page.scrape()
    amazon_page.driver.quit()
