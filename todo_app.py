import sys

class Controller():

    def get_argument(self):
        help_text = Display()
        if len(sys.argv) <= 1:
            help_text.help_display()




class Display():

    def help_display(self):
        print(
            "Python Todo application\n"
            "=======================\n"
            "\n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes a task\n"
            "-c   Completes a task)\n")

    def list_display(self):



class Model():

    def read_file():
        read_todo = open("todo.txt", "r")
        read_lines_todo = read_todo.readlines()
        todo_list = []
        for line in todo_lines:
            todo_list.append(line.split("\n"))
        read_todo.close()
        return todo_list

    