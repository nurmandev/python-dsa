# Print Exact Greeting

## Description

This project contains a simple Python function that generates a personalized greeting message using a student's name.

The function follows the required format:

```

Hello, [name]. Welcome to Talent Nation.

````

## Requirements

- Create a function called `solution`.
- Accept a student's name as an argument.
- Return the exact greeting string.
- Do not print the output.
- Do not hardcode specific names.

## Solution

```python
def solution(name):
    return f"Hello, {name}. Welcome to Talent Nation."
````

## Example

### Input

```python
solution("NURUDEN")
```

### Output

```
Hello, NURUDEEN. Welcome to Talent Nation.
```

## How It Works

1. The function receives a name as input.
2. The name is inserted into the greeting template.
3. The completed greeting is returned as a string.

## Technologies Used

* Python 3