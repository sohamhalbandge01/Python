## Taking User Input

Now we will use 'input()' to get user input. Watch this video to understand how input() function works in Python

The program then prints out the greeting using the variables `name` and `age`.

```py
name = input()
print("Hello, " + name + "!")

age = input()
print("You are " + age + " years old.")
```

input() assumes that the input is a string. \
You can convert it to an integer or numerical value using int()

```py
age = int(input())
print("You are", age, "years old.")
```

## Converting input datatype

The input() function assumes that the input is a string. This means whatever the user types, whether it is letters, numbers, or special characters, input() directly reads it as a string.

So, if you need to work with numbers, you have to convert the input to an integer or a float. We learned how to convert types in one of our previous lessons. We use the same method to convert the input to an integer:

```py
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```

If the user enters 2 as the value of num1 and 3 as the value of num2, the output will be 5. However, if we don't convert it to an integer, the output will be 23 because input() takes the input as a string, and it will perform string concatenation instead of integer addition.

## Multiple String Inputs

You've seen how to use the input() function to take input multiple times, accepting one value per line. However, sometimes you need to accept multiple inputs in a single line. To do this, you can use the split() function.

For example, if the user inputs the following:

```txt
Good Great Awesome
```

You can read these inputs like this:

```py
a, b, c = input().split()
```

The split() function breaks this single line of input into multiple parts. By default, split() divides the input based on spaces, so each word separated by a space is treated as an independent input and stored in different variables.

### Multiple integer inputs

The syntax you saw in the previous lesson takes string inputs. But if you need to take multiple integer inputs, you'll have to convert them separately.

You cannot call the int function directly on the split input as int function can only be called on one value as a time and split input has multiple values.

To handle this, you can use the map function to convert the split inputs to integers in one step. Here's how you can do it:

```py
a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c
```

What map does is, it takes the list of multiple inputs and applies the integer function to each input in the list.