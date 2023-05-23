name = input("What is your name?\n")
filename = "programming.txt"
with open(filename, 'w') as file_object:
    file_object.write("Name 1: ")
    file_object.write(name)
