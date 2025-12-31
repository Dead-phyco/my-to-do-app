FILEPATH='todos.txt'
def get_todos(filepath= 'todos.txt'):
    """ Read a text file and return the list of to-do item """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath= 'todos.txt'):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

if __name__== ' __main___':
    print('Hello')
    print(get_todos())