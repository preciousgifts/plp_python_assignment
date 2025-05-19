def modify_file_content(content):
    """Modify the file content – you can customize this."""
    return content.upper()  

def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()

        modified_content = modify_file_content(content)

        new_filename = 'modified_' + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read or write file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

read_and_write_file()
