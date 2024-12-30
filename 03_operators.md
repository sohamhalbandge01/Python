## Arithmetic Operations

In Python, you can perform various basic mathematical operations with numbers. Let's explore some commonly used arithmetic operators with examples.

### 1. Addition (+)

You can use the plus sign (+) to add two numbers.

```py
a = 6
b = 3
print(a + b)  # prints 9
```

### 2. Subtraction (-)

You can use the minus sign (-) to subtract one number from another.

```py
print(a - b)  # prints 3
```

### 3. Multiplication (*)

```py
print(a * b)  # prints 18
```

### 4. Division (/)

You can use the forward slash (/) to divide one number by another. This will give you a float (decimal number) as a result.

```py
print(a / b)  # prints 2.0
```

### 5. Integer Division (//)

You can use the double forward slash (//) to perform integer division. This will divide the numbers and return the whole number part of the result, discarding the remainder.

```py
result = 10 // 3
print(result)  # prints 3

#In this example, 10 divided by 3 equals 3.333.... The integer division returns only the whole number part, which is 3.
```

### 6. Modulo (%)

You can use the percent symbol (%), known as the modulo operator, to get the remainder of a division.

```py
print(a % b)  # prints 0

# Here, `6 modulo 3` is `0` because `6` divided by `3` leaves no remainder.
```

### 7. Exponentiation (**)

You can use the double asterisk (**) to raise a number to the power of another number.

```py
print(a ** b)  # prints 216

# In this example, `6 to the power of 3` is `216` (`6 * 6 * 6`).
```

## Assignment Operator

In Python, assignment operators are used to set or update the value of a variable. There are basic assignment operators and compound assignment operators. Let's break these down with examples for better understanding.

###  Basic Assignment Operator

The basic assignment operator is the = sign. It assigns the value on its right to the variable on its left. Here's a simple example:

```py
length = 15
```

In this example, the = operator sets the value of length to 15.

### Compound Assignment Operators

Compound Assignment Operators combine arithmetic operations with assignment. They are just a shorthand way of performing operations on a variable and assigning the result back to the variable.

Without using the compound assignment operators we write -

```py
length = 15
length = length + 5  # Updates length by adding 5 to its current value
```

The same thing using Compound Assignment Operator would be written as-

```py
length = 15
length += 5  # Shorthand for length = length + 5
print(length)  # Output: 20
```

We can use any other operator in the same way:

```txt
- x -= 5  (Subtracts 5 from `x` and assigns the result back to `x`)
- x *= 3  (Multiplies `x` by 3 and assigns the result back to `x`)
- x /= 3  (Divides `x` by 3 and assigns the result back to `x`)*
- x %= 3  (Finds the remainder when `x` is divided by 3 and assigns the result back to `x`)
```

## Relational Operators

Relational operators help you compare two values or variables. They give you a result of either True or False based on the comparison.

### Basic Comparison

Let's start with a simple example:

```py
height1 = 12
height2 = 14
print(height1 < height2) # Outputs True because 12 is less than 14

#In this example, the `<` operator compares `height1` and `height2`. Since `height1` is less than `height2`, it returns `True`.
```

### Other Relational Operators

Here are some more examples of relational operators:

```txt
- a > b   (Checks if `a` is greater than `b`)
- a == b  (Checks if `a` is equal to `b`)
- a != b  (Checks if `a` is not equal to `b`)
- a >= b  (Checks if `a` is greater than or equal to `b`)
- a <= b  (Checks if `a` is less than or equal to `b`)
```

## Logical Operators

Logical operators help you combine multiple conditions to check if they are True or False. They are often used to make decisions based on multiple criteria.

### Basic Logical Operations

Here are the basic logical operators and their usage:

#### 1. Logical AND

```py
# The AND operator returns True only if both conditions are True.

a = 7
condition = a > 5 and a < 10  # Only True if a is greater than 5 AND less than 10
print(condition)  # Output: True
```

#### 2. Logical OR

```py
# The OR operator returns True if at least one of the conditions is True.

a = 7
condition = a > 10 or a < 5  # True if a is greater than 10 OR less than 5
print(condition)  # Output: False
```

#### 3. Logical NOT

```py
# The NOT operator reverses the result of the condition. If the condition is True, `not` makes it False. If the condition is False, `not` makes it True.

a = 7
condition = not(a > 5)  # Reverses the result of a > 5
print(condition)  # Output: False
```

## Operator Precedence and Associativity

You may be familiar with BODMAS (or PEMDAS in some regions) rule for evaluating arithmetic expressions.

It says we solve parenthesis first, then divide, then multiply, then add and then subtract.

Similarly there are two main rules a program follows to evaluate an arithmetic expression:

- **Precedence** - It tells the priority of operations.
- **Associativity** - It tells what order the operations with the same priority will be performed in.

## Operator Precedence

Operator precedence determines the order in which different operators are evaluated in an expression.
Operators with higher precedence are evaluated before those with lower precedence.
This concept is similar to the rules of arithmetic, where multiplication and division takes precedence over addition and subtraction.

Here's the order of operator precedence in Python from highest to lowest:

- Parentheses: ()
- Exponentiation: **
- Unary operators: ~
- Multiplication, division, floor division, and modulus operators: *, /, //, %
- Addition and subtraction operators: +, -
- Relational operators: <, >, <=, >=
- Equality operators: ==, !=
- Logical AND operator: and
- Logical OR operator: or
- Assignment operators: =, +=, -= ... and so on

## Operator Associativity

When operators of the same precedence appear in an expression, associativity determines the order in which they are evaluated. Operators can be either left-associative or right-associative.

### Left-Associative:

On Left-Associative Operators, operations are performed from left to right. Most operators are left-associative. For instance, in (A - B + C), addition and subtraction, being left-associative, will first evaluate (A - B), and then add (C) to the result.

```py
result = 10 - 2 + 3  # Both - and + have the same precedence and are left-associative
print(result)       # Output: 11 ((10 - 2) + 3 is evaluated as 8 + 3)

result = 10 / 2 * 3  # Both / and * have the same precedence and are left-associative
print(result)       # Output: 15.0 ((10 / 2) * 3 is evaluated as 5.0 * 3)
```

### Right-Associative:

Although less common, some operators are right-associative, meaning they are evaluated from right to left. An example is the exponentiation operator **.
In (2 ** 2 ** 3) Python will first calculate (2 ** 3) which is 8 and then calculate 2^8 which evaluates to 256.

```py
result = 2 ** 2 ** 3  # Exponentiation is right-associative
print(result)        # Output: 256 (2 ** (2 ** 3) is evaluated as 2 ** 8)
```