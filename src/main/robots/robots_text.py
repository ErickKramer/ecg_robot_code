"""
Subclasses text_agent.

------
See LICENSE.txt for licensing information.
------
"""

from nluas.language.text_agent import *
import os
import sys
# sys.path.append(os.path.abspath('../'))
# from mbot_natural_language_processing.mbot_nlu.common.src.mbot_nlu.simple_phrase_divider import divide_sentence_in_phrases

class RobotTextAgent(TextAgent):
	def __init__(self, args):
		TextAgent.__init__(self, args)


if __name__ == "__main__":
	text = RobotTextAgent(sys.argv[1:])
	text.keep_alive(text.prompt)
