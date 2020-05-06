"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# ? open, second argument 'r' stands effectively for read-only
with open('/Users/kristinparrish/Desktop/code/Intro-Python-I/src/foo.txt', 'r') as file:
    # ? print all the contents - no size parameter = all contents
    print(file.read())
    # ? close the file
    file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# ? open, second argument 'w' standsfor write
with open('/Users/kristinparrish/Desktop/code/Intro-Python-I/src/bar.txt', 'w') as file:
    # ? write a string to the opened bar.txt file
    print(file.write('The answer to life\n is 42. \n Where is my towel?))
    # ? close the file
    file.close()

# ? open, second argument 'r' stands effectively for read-only
with open('/Users/kristinparrish/Desktop/code/Intro-Python-I/src/bar.txt', 'r') as file:
    # ? print all the contents - no size parameter = all contents
    print(file.read())
    # ? close the file
    file.close()
