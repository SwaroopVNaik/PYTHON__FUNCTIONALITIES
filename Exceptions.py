# Basic Syntax Of Exception Handling in Python
# Exceptions Helps us to write Really Neat Code
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
#-----------------------------------------------------------------------------------------------------------------------------
# Custom exception handling for age eligibility in voting
def check_elegibality_for_voting():
    try:
        check_age(16)
        #check_duplicate(duplicate)
        #check_address(address)
        #check_citizenship(document)
        #check_birthcertificate(document)
        #Happy Path Code
        # business Logic 
        print("Person is eligible for voting")
    except ValueError as e:
        print(e)

def check_age(age):
    if (age < 18):
        raise ValueError("Age is less then allowed limit")
    
    # Happy Path code
    # more lines of code
    print("Eligible for the voting ")
#-------------------------------------------------------------------------------------------------------------------------------------
# Call/Invoking the function :-> 👇
read_and_print_file_V1("file-ella.txt") 

# Call/Invoking the function :-> 👇
read_and_print_file_V2("file-ella.txt")

# Call/Invoking the function :-> 👇 (Custom Exception Handling Function Call)
check_elegibality_for_voting()