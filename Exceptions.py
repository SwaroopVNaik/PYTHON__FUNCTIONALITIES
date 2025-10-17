# Basic Syntax Of Exception Handling in Python
# Function Definition :-> 👇
def read_and_print_file_V1(file_path):
    file_handle = None
    try:
        # Happy_Code: Attempting to open and read the file
        file_handle = open(file_path)
        content = file_handle.read()

    except FileNotFoundError:
        """Error Handling: Implementing measures to handle situations where 
        the file may not be present or accessible."""

        print("Error: The File does not exist.")

    except PermissionError:
        print("Error: You do not have permission to access this file.")

    finally:
        """Clean Up: This block of code or instruction will execute no matter what happens,
        even if there's an error."""

        print("Clean-Up in progress....!")
        if file_handle is not None:
            file_handle.close()
#--------------------------------------------------------------------------------------------------------------------------------------
# Function Definition :-> 👇
def read_and_print_file_V2(file_path):
    file_handle = None
    try:
        # Happy_Code: Attempting to open and read the file
        file_handle = open(file_path)
        content = file_handle.read()

    except FileNotFoundError:
        """Error Handling: Implementing measures to handle situations,
        where the file may not be present or accessible."""

        print("Error: The File does not exist.")

    except PermissionError:
        print("Error: You do not have permission to access this file.")

    finally:
        """Clean Up: This block of code or instruction will execute no matter what happens,
        even if there's an error."""
        print("Clean-Up in progress....!")
        try:
            if file_handle is not None:
                file_handle.close()
        except Exception:
            # Swallow_the_Exception
            pass
#-------------------------------------------------------------------------------------------------------------------------------------
# Call/Invoking the function :-> 👇
read_and_print_file_V1("file-ella.txt") 

# Call/Invoking the function :-> 👇
read_and_print_file_V2("file-ella.txt") 
