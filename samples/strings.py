""""
Define strings and demonstrate basic operations
Strings are sequences of characters enclosed in single or double quotes
They are immutable, meaning they cannot be changed after creation

"""
# Creating strings
string1 = "Hello, World!"
string2 = 'Python Programming'

# Accessing characters in a string
first_char = string1[0]  # Accessing the first character
last_char = string2[-1]   # Accessing the last character

# String concatenation
greeting = string1 + " " + string2
print(greeting)  # Output: Hello, World! Python Programming

# String repetition
repeat_hello = string1 * 3
print(repeat_hello)  # Output: Hello, World!Hello, World!Hello

# String slicing
sub_string = string2[0:6]  # Getting a substring from index 0
print(sub_string)  # Output: Python

# String methods
upper_string = string1.upper()  # Convert to uppercase
print(upper_string)  # Output: HELLO, WORLD!

lower_string = string2.lower()  # Convert to lowercase
print(lower_string)  # Output: python programming

replace_string = string1.replace("World", "Python")  # Replace substring
print(replace_string)  # Output: Hello, Python!

# Splitting a string
words = string2.split(" ")  # Split string into a list of words
print(words)  # Output: ['Python', 'Programming']