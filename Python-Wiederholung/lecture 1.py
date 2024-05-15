# first expressions
print(1 + 1)

x = 5
print(x * 3)

# simple arithmetics
print(5 * 2.8)

print(4 * 12 / 3)

# strings
print("Hello World!")

# "Hello World!"

# Values can be stored in variables and need no specific declaration of their type
length = 20
width = 10
print(length * width)

# Multiline statements require indentation.
my_list = ["a", "B", 1, 456.78, "another string"]
for item in my_list:
    print(item)

# Jupyter Notebook and Pandas
import pandas as pd  # muss eigentlich an den Anfang der Datei
pd.Series.where

# End of line terminates a statement. If multiline statements are needed, use e.g. backslash \ (also used by the IDE)
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8

print(x)

# also ; terminates a statement. Alternatives:
x = 1
y = 2
print(x)
print(y)

x = 1; y = 2
print(x)
print(y)

# Indentation is important
for i in range(10):
    if i < 5:
        print("Lower")
    else:
        print("Higher")

# Data types and variables
x = 32
print("The variable x has the value: ", x)

y = x + 3
print(y)

x = x - 1
print(x)

# Dynamic type declaration
x = 1         # x is an integer
print(x)
x = 'hello'   # now x is a string
print(x)
x = 4.5       # now x is a float
print(x)

# x = "some string" # type conflicts
y = 23
print(x + y)

x = 2
y = 3.4
print(x * y)

# Type Conversion
first_name = "Someone"
last_name = "Orelseone"
age = 77
print(first_name + " " + last_name + ": " + str(age))

# Type Checking
x = 1         # x is an integer
print(type(x))

x = "1"         # x is a string
print(type(x))

x = [1]         # x is a list
print(type(x))

x = 1
print(isinstance(x, int))

x = "1"         # x is a string
print(isinstance(x, str))

x = 1
print(type(x))

# python ints are automatically cast to floats
x = x / 2
print(x)

x = 1.
print(type(x))

# explicit cast
x = float(1)
print(type(x))

# equality checks between floats and ints actually work
x == 1

# None Type
return_value = print('abc')
print(type(return_value))

# Boolean Type
result = (4 < 5)
print(result)
print(type(result))

# Many things are implicitly cast to booleans
print(bool(2014))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool("abc"))

# Sequential data types
x = [1, 2, "a", 4.5]   # List with elements of different types
t = (1, 2, 4, 6.7)     # Tupel
s = "a string consists of characters"

print(x[0])  # Access to 1st element
print(t[1])  # Access to 2nd element
print(s[2])  # Access to 3rd element

# Strings - A sequence of arbitrary characters enclosed in single or double quotation marks
s = 'Mostly simple quotation marks are enough'
t = "sometimes you'll need double quotation marks"

print(s)
print(t)

# Lists
# A sequence of arbitrary objects, e.g. integer numbers, float numbers, strings or (nested) lists.
# Generated with square brackets
# Elements are separated by commas; for readability it is recommended to put a space after the element (but not required)
x = [3, 99,"whatever"]
y = [42443, 5 , [5, [89, 'quite nested']], 55.7]

print(x)
print(y)

# Tupel
# Difference from lists: external: round brackets
# Tuples can no longer be changed (immutable objects)
x = (3, 99,"whatever")
y = (42443, 5 , [5, [89, 'quite nested']], 55.7)
print(x)
print(y)

# Indexing and Slicing
s = "Monty Python"
print(s[0])
print(s[-1])
print(s[2:4])

# The slicing operator can also be used with three arguments.
# The third is optional and specifies the step size s[begin, end, step]:
print(s[1:5:2])
print(s[1::3])






# txt = input("Write something: ")
# print(list(txt))
# txt = list(txt)
# txt.split()
# print(txt)
# additional = "+"
# for i in txt:
#     txt.insert(i, additional)
# print(txt)
