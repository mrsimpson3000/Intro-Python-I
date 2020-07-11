"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
from pathlib import Path

data_folder = Path(
    "C:/Users/mrsim/Projects/lambdaProjects/Intro-Python-I/src/")

file_to_open = data_folder / "foo.txt"

print(file_to_open.read_text())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file_to_create = data_folder / "bar.txt"

file_to_create.write_text("Text line one\nText line two\nText line three")
