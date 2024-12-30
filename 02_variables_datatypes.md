## Variables

A `variable` is like a labelled box where you can store data. Imagine you have a box labeled "age" and you put the number 25 in it. In Python, you would do this by writing:

```py
age = 25
```

When you write this, python creates a box(variable) with name `age`and stores 25 in that box(variable).

This process of creating a variable to store a value is called Declaration and
The process of setting its value for the first time is called Initialization.
Here's the cool part: whenever you use age in your code, Python will remember it is 25. For example, if you write print(age), Python will show 25.

```py
print(age) # Output: 25
```

## Declaring a variable

There are many different types of variables in Python. The type of a variable is defined by the kind of value it stores.

Some variable types in Python are as follows

```py
# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = 'Hello, world!'

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {'name': 'Alice', 'age': 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None
```

## Properties of Variables

We learned that variable is a labelled box which can store many different types of values. You can also change the value of a variable in your code.

For example

```py
age = 25
print(age)

# Update age
age = 26
print(age)
```

The above code will output

```py
25
26
```

Rules for Python variable names:

    - A variable name can only contain alphabets, numbers and underscores (ie. A-Z, a-z, 0-9, and _).
    - A variable name cannot start with a number.
    - A variable name cannot have spaces in between.
    - Variable names are case-sensitive (age, Age and AGE are three different variables).

## Type Conversion

In the previous problems we saw different types of datatypes. We can also convert one data type to another as per our use. This is called Type Conversion.

There are two types of Type Conversion.

### Implicit Type Conversion

Here, Python automatically converts a variable from one data type to another without the user needing to tell it to do so.

```py
x = 7
x = x/2
print(x) # Output: 3.5
```

Here’s what happens:

- Variable x is initially an integer with a value of 7
- When x is divided by 2, the result 3.5 is a float (decimal number)
- Python automatically converts x from an integer to a float

### Explicit Type Conversion

Here, we manually convert a variable from one data type to another as per our use using Python’s built-in functions

```py
num = '12'
num = int(num)
num = num + num
```

Here’s what happens:

- Initially, num is a string with the value '12'.
- We use the int() function to convert num from a string to an integer.
- After conversion, num becomes 12 (an integer), and we can perform arithmetic operations on it. If we hadn’t converted num from a string to an integer, the operation num + num would have resulted in concatenation, producing '1212' instead of 24.

## Checking the type of variables

You can check the type of any variable or value by using the type function.

```py
a = 5 
print(type(a))
```

The above code gives <class 'int'> as the output as the variable a is of type *int*.

## Converting different types of variables

```py
a = 5
print(str(a))
print(bool(a))
print(float(a))
```