## Creating a String

Strings are used for storing text. \
A string variable contains a collection of characters surrounded by double quotes.

For example:

```py
name = 'Chef'
```

## String Operations

### Concatenation

The + sign can be used between strings to add them together to make a new string.\
This is called concatenation.

For eg -

```py
x = "Good"
y = "Work"
print(x + y)   #output will be: GoodWork
```

Note: You can add spaces between words by using an empty " " with a space inside or by providing a space in the end of a word.

For e.g -

```py
x = "Good"
y = "Work"
print(x + " " + y)   #output will be: Good Work
```

## String Repetition

In Python, you can multiply strings to create a new string that repeats the original string a certain number of times. This technique is known as string repetition or string replication.

The multiplication operator (*) is used to repeat a string a specified number of times.

```py
string = "hello "
result = string * 3
print(result) # output: hello hello hello

# string is assigned the value `hello`.
# string * 3 creates a new string by repeating `hello` three times.
# The result, `hello hello hello`, is stored in the variable result and printed.
```

## Strings and Integers

Python uses the + sign for both addition and concatenation.

- Numbers are added.
- Strings are concatenated.
- We cannot mix the two

## String length

We can use the len() function to get the length of a string.

For eg.

```py
greeting = "hello"
len_string = len(greeting)
# len_string now stores the value of the length of greeting
```

## Lower and Upper case

We have other helper functions to change a string to either lowercase or uppercase.

- lower(): This function converts all characters in the string to lowercase.
- upper(): This function converts all characters in the string to uppercase.

```py
name = 'CodeChef'
lowercase_name = name.lower()
uppercase_name = name.upper()
print(lowercase_name) # Output: codechef
print(uppercase_name) # Output: CODECHEF
```

## Outputting Characters from a String

We can access the characters in a string by referring to its index number inside square brackets [ ].

This concept is known as indexing.
Indexing allows you to access individual characters in a string using their position.
The position is known as the index, and Python supports two kinds of indexing: `positive` and `negative` indexing.

- `Positive Indexing` : Starts from the beginning of the string. The first character is at index 0, the second is at index 1, and so on.

```py
s = "Codechef"
print(s[0]) # Output: C
print(s[1]) # Output: o
```

- `Negative Indexing` : Negative Indexing: Starts from the end of the string. The last character is at index '-1', the second to last is at index '-2', and so on.

```py
s = "Codechef"
print(s[-1]) # Output: f
print(s[-2]) # Output: e
```

## Changing Characters in a String

In Python, strings are immutable, which means you cannot directly update or change a character in a string.

For example

```py
myString = "Chaf"
myString[2] = 'e'
```

If you run the above program, you will get a compilation error.

However, you can create a new string with the desired changes.
Here's an example of how you can replace the character:

```py
myString = "Chaf"
myString_new = myString.replace('a', 'e')  
print(myString_new)      #This string has the correct values

# Please note that, replace() method replaces all occurrences of the provided character.
```

## String slicing

Slicing is a way to extract a part (substring) from a string.

The syntax to do that is

> substring = string[start:end]

When you specify a start index in a string slice, Python includes the character at that index as the starting point of your new substring.

The end index is exclusive. This means the character at the end index is not included in the resulting substring. The slice stops just before it.

To get the first 4 characters of a string:

```py
str = 'Interesting'
substring = str[0:4]
print(substring)
```

## String slicing

There's another syntax to slice a string:

> substring = string[start:end:step]

tep is how many characters you move forward each time you read. If your step is 1, you read one character at a time. If your step is 2, you skip one character and then read the next one.

Let's say our string is 'abcde':

```py
s = 'abcde'
print(s[0:4:2]) # Output: ac
```

Here, the step is set to 2, so it takes 2 jumps after reading each character.

The character at the start index 0 is a. Then, it jumps by 2 characters and gets c.

Once it reaches c, it stops because the end index is set to 4, so the traversal happens from index 0 to index 3.

## Changing character using slicing

You can also use slicing to change the value of a character.
We can achieve this by slicing the string into parts before and after the character to be changed, then concatenate these parts with the new character in between.

```py
string = 'Chaf'
new_string = string[:2] + 'e' + string[3:]
print(new_string) # Output: Chef
# This code modifies the string 'Chaf' to 'Chef'
```

Here's what's happening:

```py
string[:2]   # Takes the first two letters from the original word i.e, 0 to 1. In this case, it extracts 'Ch'
e            # This is the new character we want to replace the existing character at index 2 with.
string[3:]   # Takes all letters from the third index to the end. In this case, it extracts 'f'.
```

By concatenating these three parts together (string[:2] + 'e' + string[3:]), we create a new string where the original character at index 2 is replaced with 'e'.

So, new_string becomes 'Chef'.

## Reverse slicing

You can use [start:end:step] format to print a string in reverse. Let's see how.

We know when slicing, the traversal (movement) always happens from left to right. But there is a way to traverse from right to left by mentioning a negative step.

```py
s='abcde'
print(s[4:0:-1]) # Output: edcb
```

When you mention a negative step the slicing starts from right to left.
So, your start index will be 4 and the slicing stops at 1 because the end index is 0

If you had to print the entire string in reverse then you write:

```py
print(s[::-1]) # Output: edcba
```

- When you mention empty start index it will start from the very beginning,
- And if the end index is empty it goes all the way till the end,
- And since the step is negative the slicing starts from the right and goes all the to the left