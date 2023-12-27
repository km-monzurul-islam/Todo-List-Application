Todo List Application
This is a simple console-based Todo List application written in Python.

Table of Contents
=================
Introduction
Features
Usage
Project Structure
License
Introduction
The Todo List Application allows users to manage their tasks through a command-line interface. Users can view all existing tasks, add new tasks, remove tasks, and exit the application.

Features
========
View all Todos
Add a new Todo
Remove an existing Todo
Exit the application

Usage
=====
Run the main.py script in your Python environment.
Follow the on-screen menu prompts to interact with the Todo List application.
Choose options to view, add, or remove Todos.
Exit the application when done.

Project Structure
=================
main.py: The main script that orchestrates the Todo List application.
todo_list.py: Defines the TodoList class, responsible for managing Todo items.
utilities.py: Contains utility functions, such as displaying the menu.

TodoList Class
The TodoList class has the following methods:
__init__(self): Initializes an instance of the TodoList with an empty list.
add_todo(self): Adds a new Todo to the list.
remove_todo(self): Removes a Todo from the list.
see_all_todos(self): Displays all existing Todos.
__repr__(self): Provides a string representation of the TodoList instance.

Utilities Module
The utilities module includes the show_menu() function, which displays the available options in the application menu.

License
This project is licensed under the MIT License.