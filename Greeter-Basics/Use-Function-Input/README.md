# Student Learning Track Profile

## Description

This project contains a simple Python function that creates a student's learning track profile message using the student's name and chosen track.

The function returns the message in the exact format:

```

[name] is starting the [track] track.

````

## Requirements

- Create a function called `solution`.
- Accept two arguments:
  - `name` — student's name
  - `track` — learning track
- Return the final sentence.
- Do not print the output.

## Solution

```python
def solution(name, track):
    return f"{name} is starting the {track} track."
````

## Example

```python
solution("Nuru", "Python")
```

Output:

```
Nuru is starting the Python track.
```

## Technologies Used

* Python 3