
# Data Types in Python

# Strings
a = "Hello World"
b = 'Hello World'
c = str(1234)

# Integer
d = 123
e = int(c)
j = 10_000_000_000

# Float
f = 0.2
g = float(123)
h = 123.0
i = 1e10

# Boolean
b1 = True
b2 = False
b3 = bool("Hello World")   # bool() works on almost everything
bool("False")
bool("0")
bool(0)
bool("")

# often found in constructs like
number = 0
while not number:
    number = int(input("please enter a number other than zero: "))

# List
a = [1, 2, 3]  # GOOD PRACTICE: collect things of the same type
a.append(4)    # mutable
a
list("Hello World")
str(a)
y = [str(x) for x in a]
';'.join(y)

# Tuple
t = (1, 2, 3)
s = (777, "Hello", "Spiced")  # different type OK
tuple("Hello")
tuple(a)
a = 7
b = 2
b, a = a, b  # swapping variables with implicit tuples

# Dictionary
d = {'cat': 'Katze', 'dog': 'Hund', 'fish': 'Fisch'}
d['dog']

# mutable: list, dict, set
# immutable: all others

# basic: int, str, float, bool, NoneType
# composite: list, tuple, dict, set

# shuffling only works with lists
import random
t = [1,2,3,4,5,6,7]
random.shuffle(t)
t

# checking the type of variables
type(a)

# skip
set
NoneType


# tomorrow
DataFrame
