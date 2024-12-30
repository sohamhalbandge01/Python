## Creating Arrays

Arrays in Python are commonly referred to as lists.

Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

In Python, list is denoted by square brackets []

- It can hold elements of different data types, such as numbers, strings, or even other lists.
- Lists are mutable, which means you can modify them by adding, removing, or changing elements.

```py
# Consider the list  'fruits'  and  'numbers'  below
fruits = ["apple", "banana", "orange", "grape"]

numbers = [20, 10, 0, -5]
```

## Index & printing specific elements of an Array

You access an array element by referring to the index number inside square brackets [].

Similar to what we saw in strings, list items are indexed and you can access them by referring to their index number:

```py
            0      1      2      - index numbers
         ["red","Green","Blue"]  - the list
# Note - Indexing always start from 0 when going left to right.
```

To access a particular element of an array, we use the same syntax we used to access a character of a string

```py
arr = ["red","Green","Blue"]
# to access the third element of the array:
print(arr[2]) # Output: Blue
```

## Changing the elements of an Array

You can also modify elements in a list by assigning a new value to a specific index.

```py
fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = "kiwi"
print(fruits)  # Output: ["apple", "kiwi", "orange", "grape"]
```

## Displaying the count of elements

To get the length of an array or the number of elements present in an array, you can use the len() operator:

For e.g.

```py
myNumbers = [10, 20, 30, 40, 50]
print(len(myNumbers))      # will output 5
```

## Negative Indexing

List items can also be negatively indexed:

```py
            -3      -2     -1      - index numbers
         ["red","Green","Blue"]  - the list
```

Note - Indexing always starts from -1 when going right to left.

## Slicing a list
Similar to what we saw in slicing of strings, you can slice lists as well.

You can specify a range of consecutive indexes by specifying where to start and where to end the range in this manner - print(list[1:4]).

This will print elements from index number 1 to 3.

Note:

- Indexing starts from 0.
- Item on index no 4 will not be printed as the end index is excluded.
For eg -

```py
a = ["Juke", "King", "Hearts", "68", "Kite"]
print(a[1:4])
# Output : ["King", "Hearts", "68"]
```

## Operations on Lists

So far, we've learned how to access list items using indexing and slicing.
As you move ahead on lists, you will want to do more than fetch items from the lists.
Python allows you even to update and modify lists.

There are four major functions that you can use to update any given list and its items.

1. append()
This function helps you to add a new item at the end of the list.

2. insert()
This function helps you to add a new item at a specific position in the list. You can exactly specify which position you want to add the new item.

3. remove()
This is used to remove the first matching element from a list. You can exactly specify which item you want to remove from the list.

4. pop()
This is used to remove the element at the specified position.

Let us try to understand how each of these functions works in depth in the following video. Use the concepts to solve the upcoming problems in this lesson.

### List Append

To add an item to the end of a list, we use the append() function.

```py
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) # Output: ["apple", "banana", "cherry", "orange"]
```

In the append() function, you provide the item you want to add, and it will be added to the end of the list.

### List Insert

Another function that helps us add elements to a list is the INSERT() function.

While the APPEND() function adds elements to the end of the list, the INSERT() function allows us to specify the index where we want to insert the new element.

```py
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits) # Output: ["apple", "orange", "banana", "cherry"]
```

With the INSERT() function, we specify the position where we want to add the new item (using an index) and the item we want to add.

When we insert a new item into the list, it is placed at the specified position, and the rest of the items are shifted to the right to make room for it.

In the example above, "ORANGE" is added at index 1, so "BANANA" and "CHERRY" are shifted to the right.

### List remove

We learned how to add items to a list, and now we'll see how to remove items.

To remove an item, we use the remove() function.

This function removes the first occurrence of the specified item from the list.

```py
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits) # Output: ["apple", "cherry", "banana"]
```

Here's how it works:

- You call the remove() function and pass the item you want to remove.
- The function searches for the first occurrence of that item in the list.
- Once it finds the item, it removes it from the list.
- In the example above, the first occurrence of BANANA is removed, leaving the list as ["apple", "cherry", "banana"].

### List pop

There's another function to help you remove items from a list.

The POP() function lets you take an item out of the list, but you can choose whether to remove the last item or an item from a specific position.

1. If you don't tell pop() which item to remove, it will take out the last item in the list.

```py
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits) # Output: ["apple", "banana"]
```

2. You can also tell POP() which item to remove by giving it the position (index) of the item. For example, let's say you want to remove the item at index 1 (which is "banana"):

```py
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
removed_fruit = fruits.pop(1)
print(removed_fruit) # Output: cherry
print(fruits) # Output: ["apple"]
```

- You call the POP() function and pass the index of the item you want to remove.
- The function removes the item at that position and returns it to you.

### List concatenation

We have learned about various operations we can perform on lists.
Another simple operation you can do with lists is list concatenation.

When you use the addition operator on two lists, it combines them into one longer list, placing all the items from both lists together.

```py
fruits1 = ["apple", "banana"]
fruits2 = ["cherry", "date"]
all_fruits = fruits1 + fruits2
print(all_fruits) # Output: ["apple", "banana", "cherry", "date"]
```

When we concatenate (combine) two lists using the + operator, it creates a new list that includes all the items from the first list followed by all the items from the second list.

### List String User Input

Imagine you want to create a list based on the items a user enters.
Instead of hardcoding the list items, you can ask the user to provide them.

You can take a list of items from the user by using the INPUT() function and then splitting the input into individual items.

- Use the INPUT() function to read the user input items separated by spaces.
- Use the SPLIT() function to break the input string into individual items and store them in a list.

```py
fruits = input().split()
print(fruits)
```

If the user enters

```
apple banana cherry date
```

The SPLIT() function will break this input string into individual items based on the spaces and create a list like this:

```py
print(fruits) # Output: ["apple", "banana", "cherry", "date"]
```

- User Input: The INPUT() function reads a line of text input from the user.
- Splitting the Input: The SPLIT() function, splits the input string at each space and returns a list of words.

NOTE:

When using input().split(), the input is read as a string by default.
If you need to read integer inputs, you'll need to convert these string inputs into integers. 

### List Integer User input

If you want to take a list of numbers as input, you need to convert each input from a string to an integer.

Here’s how you can achieve that:

- Read User Input: When you need to input a series of numbers, each number is initially read as a string.
- To use these numbers in numerical operations, you must convert them from strings to integers.
- Convert to Integers: Use the MAP() function to apply the INT() function to each item, converting them from strings to integers.
- Create a List: LIST() function collects these elements into a list.
- This list of integer values is stored inside a variable

```py
numbers = list(map(int, input().split()))
```

If the user enters:

```py
1 2 3 4 5
```

The MAP() function will convert each item from a string to an integer, and LIST() will create a list of these numbers:

```py
print(numbers) # Output: [1, 2, 3, 4, 5]
```