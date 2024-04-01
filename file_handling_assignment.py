def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Data entry")
            file.write("number 1234")
            file.write("Last line")
    except IOError as e:
        print("Error creating file:", e)

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("First line")
            file.write("new line")
            file.write("other line")
    except IOError as e:
        print("Error appending to file:", e)

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
