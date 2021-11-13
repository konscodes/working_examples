def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


'''
- Open the file in append & read mode (‘a+’). Both read & write cursor points to the end of the file.
- Move read cursor to the start of the file.
- Read some text from the file and check if the file is empty or not.
- If the file is not empty, then append ‘\n’ at the end of the file using write() function.
- Append a given line to the file using write() function.
- Close the file
'''