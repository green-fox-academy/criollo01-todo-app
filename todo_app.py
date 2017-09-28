import sys

class Controller():

    def get_argument(self):
        help_text = Display()
        if len(sys.argv) <= 1:
            help_text.print_usage()
        list_todo = Display()
        if sys.argv[1] == "-l":
            list_todo.list_display()
        elif sys.argv[1] == "-a":
            if sys.argv[2:] == []:
                print("Unable to add: no task provided.")
            else:
                add_todo = Model()
                add_todo.add_task()
                list_todo.list_display()
        elif sys.argv[1] == "-r":
            if sys.argv[2:] == []:
                print("Unable to remove: no index provided")
            else:
                pass
        elif sys.argv[1] == "-c":
            if sys.argv[2:] == []:
                print("Unable to check: no index provided")
            else:
                pass
        else:
            print("\nUnsupported argument")
            help_text.print_usage()


class Display():

    def print_usage(self):
        print(
            "\n"
            "Python Todo application\n"
            "=======================\n"
            "\n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes a task\n"
            "-c   Completes a task)\n")

    def list_display(self):
        read_list = Model()
        read_list.read_file()
        if read_list.read_file() == []:
            print("No todos for today! :)")
        else:
            serial = 0
            for task in read_list.read_file():
                serial += 1
                if task[0] == "0":
                    print(serial, "[ ] - ", task[0])
                elif task[0] == "1":
                    print(serial, "[x] - ", task[0])


class Model():

    def read_file(self):
        read_todo = open("todo.txt", "r")
        read_lines_todo = read_todo.readlines()
        todo_list = []
        for line in read_lines_todo:
            todo_list.append(line.split("\n"))
        read_todo.close()
        return todo_list

    def add_task(self):
        append_todo = open("todo.txt", "a")
        check_text = "".join(sys.argv[2:])
        append_text = "" + check_text + "\n"
        append_todo.writelines(append_text)
        append_todo.close()
        print("Task added successfully.")

    def remove_task(self):
        pass

    def check_task(self):
        pass


control = Controller()
control.get_argument()
