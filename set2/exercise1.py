"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# this line stores words into a list called "some_words"
some_words = ["what", "does", "this", "line", "do", "?"] 

#This line prints the words in the list "some words" one by one
for word in some_words:
    print(word)

#This line prints the words in the list "some words" one by one but changed "word" into "x"
for x in some_words:
    print(x)

print(some_words)

# if the length of the words in "some words" is greater then 3, then "some_words contains more than 3 words" will be printed.
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# define a function called "uselfulFunction"
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """

# print tveryting inside () which is got from "platform.uname"
    print(platform.uname())

# to exeute the codes above.
usefulFunction()
