import os # -> Std_Lib_Function
"""
Create a File -> 
-> This Functions Creates A file.
-> "w" -> Creates a New File or Overwrites the Existing File
-> With -> This Statement serves as context Manager In Python, which simplifies resource management, particularly working with files
"""
def Create_File(File_Name):
    with open(File_Name, "w") as file_Handle:
        file_Handle.close()

"""
Appending/Updating the File -> 
-> The Function adds new data at the end of the file.
-> "a" -> when we open the a file append mode, adding new data at the end of the file without overwriting the existing data
"""
def append_Contents(File_name, content):
    with open(File_name, "a") as file_Handle:
        file_Handle.write(content)
        file_Handle.write(content)
        file_Handle.write(content)
        file_Handle.close()
"""
-> Reading/Printing the Contents of the File ->
-> This Functions Reads the Contents of the FIle
-> "r" -> This Functions reads/prints the contents of the File
"""
def read_print_content(File_name):
    with open(file_name, "r") as file_Handle:
        content = file_Handle.read()
        print(content)
        file_Handle.close()

"""
-> Delete the contents of the file -> 
-> We use import os in Python for file deletion because it provides access to operating system functionalities, allowing us to easily delete files with the os.remove() function and manage file paths efficiently across different platforms.
"""
def delete_file(File_Name):
    # To check if the File exists ->
    if os.path.exists(File_Name):
        os.remove(File_Name) # There is not delete in os we hae to use (os.remove) to delte the file
        print(f"The File got deleted -> {File_Name}")
    else:
        print("The File doesn't exists")

# Invoking/ Calling the Functions of File :->
# Inputs :->
file_name = "my_python_notes.text"
Info = "Namaskara Bharat..!\n"

# Invoking the Functions :->
Create_File(file_name)
append_Contents(file_name, Info)
read_print_content(file_name) 
delete_file(file_name)