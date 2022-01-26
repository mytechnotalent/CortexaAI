# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import os
from gtts import gTTS


class Speak:
    """
    Class to handle text to speech
    """

    def __init__(self):
        pass

    @staticmethod
    def speech(m_text):
        """
        Method to handle text to oh speech

        Params:
            m_text: str
        """
        language = 'en'
        m_text = gTTS(text=m_text, lang=language, slow=False)
        m_text.save('text.mp3')
        os.system("mpg321 -q text.mp3")
