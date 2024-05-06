try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Line 3: Hello, world!\n")
        
    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
        
    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Additional text\n")
        file.write("67890\n")
        file.write("Line 6: Appended line\n")
        
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File handling completed.")

