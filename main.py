import utilities
from todo_list import TodoList

todo_list = TodoList()

print("Todo List Application")

while(True):
    utilities.show_menu()
    userChouse: str = input("\nWhat do you want to do? ").lower()
    if userChouse == "s":
        todo_list.see_all_todos()
    elif userChouse == "a":
        todo_list.add_todo()
    elif userChouse == "r":
        todo_list.remove_todo()
    elif userChouse == "e":
        print("The program is exiting...")
        break
    else:
        print("Incorrect Input")

