try:
    with open('example.txt', 'r') as file:
        data = file.read()
        print(data)
    with open('example.txt', 'w') as file:
        file.write("Hello. This is my file test file for python file and exception handling.")
except FileNotFoundError:
    print("The file does not exist.")