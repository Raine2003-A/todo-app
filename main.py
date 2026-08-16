#from functions import get_todos, write_todos
# can also use this and write just get_todos() in case of small module

import functions
import time

now = time.strftime("%b %d, %Y  %H:%M:%S")
print("It is ", now)

while True:
    user_input = input("Type add, show, edit, completed and exit: ")
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith("add"):
        add_todo = user_input[4:] +'\n'

        #file = open('todos.txt','r')
        #todos = file.readlines()
        #file.close()

        todos = functions.get_todos()

        todos.append(add_todo)

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}- {item}"
            print(row)



    elif user_input.startswith("edit"):
        try:
            num = user_input[5:]
            num = int(num)
            num = num - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo to replace: ")
            todos[num] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Incorrect command! Please enter the serial number to edit.")
            continue

    elif user_input.startswith("completed"):
        try:
            num = user_input[10:]
            num = int(num)

            todos = functions.get_todos()

            index = num-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f" Todo - {todo_to_remove} is removed from the list"
            print(message)

            functions.write_todos(todos)

        except IndexError:
            print("This item does not exist. Please enter a valid index.")
            continue



    elif user_input.startswith("exit"):
        break

    else:
        print("Command is invalid!")

print('Bye')