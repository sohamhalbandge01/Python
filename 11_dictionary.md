A dictionary is an unordered collection of data in a key-value pair format. \

Each value in a dictionary is accessed using a unique key.

## Creating a dictionary

```py
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
```

- Dictionaries are created using curly braces {}.
- Key-value pairs are separated by colons : and elements are separated by commas.

## Accessing values

Values in a dictionary are accessed using keys.

```py
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # Access the value for the key "name"
```

## Dictionary characteristics

- `Order`: Unlike sequences (e.g., lists, tuples), dictionaries are not ordered till python versons older than 3.7. After v3.7, they are ordered.
- `Mutable`: Dictionaries can be modified (items can be added, removed, or modified).
- `Unique`: Keys in a dictionary must be unique.

## Modifying a dictionary

Adding items to a dictionary - To add a new key-value pair to a dictionary, you simply assign a value to a new key.

```py
my_dict = {"name": "Alice", "age": 30}
my_dict["location"] = "New York"
```

Modifying Items in a Dictionary - To modify an existing value associated with a key in a dictionary, you can simply reassign a new value to that key.

```py
my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31  # Update the value for the key "age"
```

## Removing items from a dictionary

Removing items from a dictionary involves deleting key-value pairs. \
Dictionaries provide different methods to remove elements based on keys.

- `del`: Allows you to remove a specific key-value pair from the dictionary.

```py
my_dict = {"name": "Alice", "age": 30}
del my_dict["age"]  # Remove the key "age" and its corresponding value
```

- `pop()`: Removes a specified key and returns the corresponding value.

```py
my_dict = {"name": "Alice", "age": 30}
removed_age = my_dict.pop("age")  # Remove the key "age" and retrieve its value
```

- `clear()`: Removes all key-value pairs from the dictionary, leaving it empty.

```py
my_dict = {"name": "Alice", "age": 30}
my_dict.clear()  # Clear all key-value pairs
```

## Iterate over a dictionary

Iterating over a dictionary in Python allows you to access and process its elements, which are key-value pairs.

### Iterating Over Keys:
By default - iterating over a dictionary iterates over its keys.

```py
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for key in my_dict:
    print("Key:", key)
```

### Iterating Over Values:

```py
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for value in my_dict.values():
    print("Value:", value)
```

### Iterating Over Key-Value Pairs:
To iterate over key-value pairs, you can use the items() method.

```py
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for key, value in my_dict.items():
    print("Key:", key, ", Value:", value)
```

## Key existence in a dictionary

It's important to determine whether a particular key exists before attempting to access its associated value to avoid potential errors.

- `in`: Can be used to check if a specific key is present in a dictionary.

```py
my_dict = {"name": "Alice", "age": 30}
print("name" in my_dict)  # Output: True
print("location" in my_dict)  # Output: False
```

- `get()` : Allows you to retrieve the value for a given key if it exists.

```py
my_dict = {"name": "Alice", "age": 30}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("location"))  # Output: None
```

## Nested Dictionary

A nested dictionary is a dictionary that contains another dictionary (or dictionaries) as a value for one or more of its keys. This means that the values of a dictionary can themselves be dictionaries.

```py
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
```

To access values in a nested dictionary, you use multiple square brackets to access the value of a specific key at each level.

```py
print(nested_dict["person1"]["name"])  # Output: Alice
print(nested_dict["person2"]["age"])   # Output: 25
```

You can modify values in a nested dictionary by accessing the specific keys and assigning new values.

```py
nested_dict["person1"]["age"] = 35
nested_dict["person2"]["location"] = "New York"
```