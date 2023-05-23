from name_function import get_formatted_name

print("Enter q at any time to quit.")
while True:
    first = input("\nPlease input the first name.\n")
    if first == "q":
        break
    middle = input("\nPlease input the first name.\n")
    if first == "q":
        break
    last = input("Please input the last name.\n")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"Neatly formatted name: {formatted_name}")