name = input("What is your name?\n")
filename = "programming.txt"
with open(filename, 'a') as file_object:
    file_object.write("Name 2: ")
    file_object.write(name)
