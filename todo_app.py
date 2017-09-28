import sys
import os

class Controller(object):
    help_text = Display()
    if len(sys.argv) == 1:
        help_text.help_display()