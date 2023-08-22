# Specify the file name
file_name = "example.txt"

# Content to write to the file
file_content = """This is an example text file.
It contains multiple lines of text.
Each line is separated by a newline character."""

# Open the file for writing
with open(file_name, "w") as file:
    file.write(file_content)

print(f"File '{file_name}' has been created and written.")
