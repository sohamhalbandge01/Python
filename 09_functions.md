Functions allow you to break down a complex program into smaller, manageable modules.

Each function can represent a specific task or functionality.

Once defined, functions can be reused in different parts of the program or even in different programs, promoting code reuse and saving development time.

## Anatomy of a function

Let us breakdown the structure of a function.

```py
def function_name(parameters):
    # Function body (code block)
    # ...
    return result  # Optional return statement
```

- `def`: Keyword to define a function.
- `function_name`: Name of the function (should be descriptive).
- `parameters`: Inputs that the function accepts (can be optional).
- `Function body`: Code block where the function performs its task.
- `return`: Optional statement to return a value from the function.

## Return values

Functions in Python can serve two primary purposes when it comes to providing information to the caller: they can either return a value or print an output.

## Returning Values from Functions:

When a function returns a value, it's providing a piece of data back to the caller. \
This data can be used for further processing, assignment to variables, or any other purpose within the program. The return statement is used to send a value back to the caller. \

Check the sample below

```py
def calculate_square(num):
    square_result = num * num
    return square_result

# Calling the function and capturing the return value
result = calculate_square(5)

print("Square of 5:", result)  # Output: Square of 5: 25
```

## Printing Output from Functions:

A function can also directly print output to the console using print statements.
However, this doesn't provide any data back to the caller in a way that can be used elsewhere in the program.
The primary purpose here is to display information, not to provide data for further processing.
Check the example below which gives the same output as the code above

```py
def print_square(num):
    square_result = num * num
    print("Square of", num, "is:", square_result)

# Calling the function
print_square(5)  # Output: Square of 5 is: 25
```

## Parameters, Arguments

Note that there is a difference between 'PARAMETERS' and 'ARGUMENTS'. \
'Arguments' are actual values passed to a function.

Check the code template below

```py
# `a`, `b` are `Parameters` inside the function
# `A`, `B` are `Arguments` passed to the function

def add_numbers(a, b):
    return a + b

# Calling the function with arguments
A = 5
B = 3
result = add_numbers(A, B)
print("Sum:", result)
```

## Variable Scope

Scope in Python can be broadly categorized into two types: global scope and local scope

## Global scope

- Variables defined outside of any function have global scope.
- These variables can be accessed from anywhere in the code, both inside and outside functions.

```py
global_var = 10

def my_function():
    print(global_var)  # Accessing the global variable

print(global_var)  # Accessible here
my_function()  # Accessible here
```

Output

```txt
10
10
```

Once we defined the global_var at the top, it can be used anywhere in the code.

## Local Scope

- Variables defined within a function have local scope, meaning they are accessible only within that function.
- Local scope is limited to the function where the variable is defined.

```py
def my_function():
    local_var = 20  # Local variable
    print(local_var)  # Accessible here

print(local_var)  # Error: local_var is not defined (outside its scope)
```

Because the local_var was defined inside the function, you cannot print it outside the function.

## Accessing Variables from Different Scopes

- A function can access variables in its local scope, as well as variables in the global scope.
- However, a local variable will take precedence over a global variable if they have the same name.

## Calling a function within function

Functions can also call other functions in Python.

Check the sample code given below

```py
# Function to calculate the square of a number
def square(num):
    return num * num

def square_and_double(num):
    # Call the square function to calculate square
    squared = square(num)

    # Double the squared result
    return 2 * squared

# Call the square_and_double function with the argument 3
result = square_and_double(3)

print("Result:", result)     # Output will be 'Result: 18'
```