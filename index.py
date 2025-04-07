def file_editor():

    filename = input("Enter the name of the file you want to read: ")

    try:
        with open(filename, 'r') as the_file:
            the_file.read()
            print(the_file.read(), "\n File read successfully.")
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission Denied")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")
        
    contents = input(f"Enter the contents you want to write to the file: ")
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(contents)
            print("\n File written successfully.")
    except Exception as e:
        print(f"Failed to write new file: {e}")

file_editor()
# This code is a simple file editor that allows the user to read and write to a file.
