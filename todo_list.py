class TodoList:
    def __init__(self):
        self.__list: list = []


    def add_todo(self) -> None:
        while(True):
            user_input = input("Enter the TODO description: ").strip().capitalize()

            if not user_input:
                print("The description cannot be empty.")
                continue

            if user_input in self.__list:
                print("The description must be unique.")
                continue

            self.__list.append(user_input)
            print(f"TODO successfully added: [ {user_input} ].")
            break


    def remove_todo(self) -> None:
        if not self.__list:
            return print("No TODOs have been added yet.")
        
        while(True):
            self.see_all_todos()
            user_input = input("Select the index of the TODO you want to remove: ")

            if not user_input:
                print("Selected index cannot be empty.")
                continue

            try:
                user_input_number = int(user_input)
            except ValueError as error:
                print("The given index is not valid.")
                continue

            if user_input_number > len(self.__list):
                print("The given index is not valid.")
                continue
            
            print(f"TODO removed: [ {self.__list.pop(user_input_number - 1)} ].")
            break

    def see_all_todos(self) -> None:
        for index, todo in enumerate(self.__list):
            print(f"{index + 1}: {todo}")
    

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"