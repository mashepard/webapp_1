FILEPATH = 'C:/Users/mshep_000/PycharmProjects/pythonProject/files/todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read text file, return a list of item """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to dos item list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



# this will only execute if functions.py is executed directly
if __name__ == "__main__":
    print("hello")