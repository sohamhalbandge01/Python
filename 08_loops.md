## Loops

A loop in programming is like doing something over and over again until you're satisfied.
You get to pick what you want to do and how many times you want to do it.
It's like telling the computer, "Keep doing this until I say stop!"

Using loops makes things easier because instead of writing the same instructions multiple times, you can just tell the computer to repeat those instructions for you.

Imagine you want to print numbers from 1 to 10, each on a new line.

Without using a loop, you'd have to write 10 separate print statements like this:

```py
print(1)
print(2)
print(3)
# And so on, until print(10)
``` 

But if you use LOOPS, this can be done with just a single print statement. We'll learn how to do this using different programming constructs in the upcoming lessons

## While loop

LOOPS can execute a block of code as long as a specified condition is reached.
They are handy because they save time, reduce errors, and they make code more readable.

The WHILE LOOP loops through a block of code as long as a specified condition is true:

```py
while (condition):
    // code to be executed
```

Example

```py
counter = 0
while counter < 5:
    print("The counter is:", counter)
    counter = counter + 1
```

In the example above, the WHILE loop is executed as long as the condition 'counter < 5' is true.

The initial value of 'counter' is 0.

The code block inside the loop prints the value of Counter and increments it by 1 with the statement Counter = Counter + 1.

The loop will continue executing until 'counter' becomes equal to or greater than 5.

## For Loop

When you know exactly how many times you want to loop through a block of code, use the for loop instead of while loop.
FOR loop in Python is designed to iterate over a sequence of elements, such as a list, string, or range of numbers.

Example 1: Iterating over a list

```py
fruits = ["apple", "banana", "orange"]
for item in fruits:
    print(item)
```

The For loop iterates over each element in the fruits list.
On each iteration, the item variable takes the value of the current element, and it is printed.
The output will be:

```py
apple
banana
orange
```

Note:

- There was no increment in the For loop syntax.
Unlike While loop - we did not need to write 'item = item + 1' or any such syntax
- item is just a Variable. You can replace it with element / i / x or any other Variable.

### For loop can also be used to iterate over a string.

```py
name = "Alice"
for char in name:
    print(char)
```

Here, the For loop iterates over each character in the 'name' string. \
The 'char' variable takes on the value of each character, and it is printed. \
The output will be:

```txt
A
l
i
c
e
```

### Range of numbers

In Python, you can use a for loop to iterate over a sequence of numbers.  \
The Range() function helps generate this sequence, allowing you to define where to start, where to stop, and how much to increment by.

The basic syntax for using the Range() function in a for loop is:

```py
for i in range(start, stop, step):
    # do something
```

How It Works: When you provide three arguments to range(start, stop, step), it generates numbers starting from start, up to (but not including) stop, incrementing by step.

For example:

```py
for i in range(0, 10, 2):
    print(i)
```

Gives the Output:

```py
0
2
4
6
8
# Let's see what's happening in the example given above:
# Start: The first number in the sequence. In range(0, 10, 2), the sequence starts at 0.
# Stop: The number where the sequence ends, but it is not included in the sequence. In range(0, 10, 2), the sequence stops before 10.
# Step: The difference between each number in the sequence. In range(0, 10, 2), the sequence increments by 2, generating numbers 0, 2, 4, 6, 8.
```

### Two range arguments

Another way to use the range function is by providing two arguments: start and stop. \
When you use two arguments in the range(start, stop) function, it generates a sequence of numbers starting from the start value up to, but not including, the stop value.

```py
for i in range(2, 6):
    print(i)
```

Output:

```py
2
3
4
5
# Start: The sequence starts at the start value (inclusive). In this example, it starts at 2.
# Stop: The sequence ends at the stop value (exclusive). In this example, it stops before 6.
```

So, the range(2, 6) function generates the numbers 2, 3, 4, and 5. The start value is included in the sequence, but the stop value is not.

### Single range argument

You can also pass just one argument to the range function. \
When you use one argument in the range(n) function, it generates a sequence of numbers starting from 0 up to, but not including N.

```py
for i in range(5):
    print(i)
```

Expected Output:

```py
0
1
2
3
4
# The sequence starts at 0 and ends at n-1. In this example, it generates numbers from 0 to 4.
```

So, the above loop runs 5 times. The range(5) function generates the numbers 0, 1, 2, 3, and 4. \
This is useful when you need to repeat something a specific number of times.

## Break Statement

The break statement is a control statement in Python that allows you to exit a loop prematurely.

- When the break statement is encountered inside a loop, the loop is immediately terminated
- The program execution continues with the next statement after the loop

Example:

```py
fruits = ["apple", "banana", "orange", "grape"]

for item in fruits:
    if item == "orange":
        break
    print(item)
```

Output:

```txt
apple 
banana
```

In this example, the FOR loop iterates over each fruit in the fruits list. \
Inside the loop, there is an if statement that checks if the current fruit is equal to "orange". \
When the condition becomes true, the break statement is executed, and the loop is immediately terminated.

## Continue Statement

The continue statement skips one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.

Example:

```py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
```
