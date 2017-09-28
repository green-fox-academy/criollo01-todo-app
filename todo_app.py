import sys
import os

class Controller(object):
    help_text = Display()
    if len(sys.argv) == 1:
        help_text.help_display()







class Display(object):
    def help_display(self):
        return print(
                    "Python Todo application\n"
                    "=======================\n"
                    "\n"
                    "Command line arguments:\n"
                    "-l   Lists all the tasks\n"
                    "-a   Adds a new task\n"
                    "-r   Removes a task\n"
                    "-c   Completes a task)\n")

)