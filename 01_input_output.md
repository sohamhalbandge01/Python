## Printing a number

We use print() function

```py
print(12)
```

## Printing text

To print text, there is only one difference. All textual content should start and end with either double quotes(" ") or single quotes(' ').

For e.g. 

```py
print("I love Python") # Output: I love Python
print('I love Python') # Output: I love Python
```

These two lines perform identical tasks; the first utilizes double quotes, while the second uses single quotes.

## Arithmetic Operations

We can also perform mathematical operations using `print`.

```py
print(2+4) # Output: 6
```

The above code will output the result of the mathematical operation, which is 6.

**NOTE**: If you enclose the operation within quotes, the entire operation will be treated as text (a string) and will be printed exactly as it is.

```py
print("2 + 4") # Output: 2 + 4
```

In this case, the output will be the string "2 + 4" instead of the result of the addition.

- Without quotes: The expression is evaluated, and the result is printed.
- With quotes: The expression is treated as a string and printed as it is.

Understanding this distinction is important for correctly displaying the results of calculations versus showing text.

## Multiple Outputs

You can add as many print statements as you want to your program. Each print statement outputs its content on a new line.

```py
print("99")
print(100)
```

Output:

```py
99
100
```

## Outputs on the same line

We can print multiple items by separating by commas. Python will automatically add a space between them.

```py
print(1, 2, 3, 4) # Output: 1 2 3 4
```

When you use commas to separate items inside the print() function, Python prints each item with a space in between.

## Inserting text Between Outputs

Remember that to print multiple values on same line, we have to use comma inside print statement.

We can also combine text and numbers in a single print statement by comma separating them.

For example, check the below code:

```py
print("My favorite number is", 10)

# Output: My favorite number is 10
```
