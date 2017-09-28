import sys

class Controller():

    def get_argument(self):
        help_text = Display()
        if len(sys.argv) <= 1:
            help_text.help_display()
        list_todo = Display()
        if sys.argv[1] == "-l":
            list_todo.list_display()
        elif sys.argv[1] == "-a":
            if sys.argv[2:] == []:
                print("Unable to add: no task provided.")
            else:
                add_todo = Action()
                add_todo.add_task()
                list_todo.list_display()
        elif sys.argv[1] == "-r":
            if sys.argv[2:] == []:
                print("Unable to remove: no index provided")
            else:

        elif sys.argv[1] == "-c":
            if sys.argv[2:] == []:
                print("Unable to check: no index provided")
            else:

        else:
            print("Unsupported argument")
            help_display.help_text()


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
        read_list = Action()
        read_list.read_file()
        if read_list.read_file() == []:
            print("No todos for today! :)")
        else:
            serial = 0
            for task in read_list.read_file():
                serial += 1
                if task[0] == "0":
                    print(serial, "[ ]", " - ", task[1][:-1])
                elif task[0] == "1":
                    print(serial, "[x]", " - ", task[1][:-1])

class Actions():

    def read_file(self):
        read_todo = open("todo.txt", "r")
        read_lines_todo = read_todo.readlines()
        todo_list = []
        for line in todo_lines:
            todo_list.append(line.split("\n"))
        read_todo.close()
        return todo_list

    def add_task(self):
        append_todo = open("todo.txt", "a")
        check_text = " ".join(sys.argv[2:])
        append_text = " " + check_text + "\n"
        todo_file.writelines(append_text)
        todo_file.close()
        print("Task added successfully.")
