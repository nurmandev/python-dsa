# Student Badge Generator

## Description

This project contains a simple Python function that creates a three-line student badge using a student's name and cohort.

The badge format is:

```

Name: [name]
Cohort: [cohort]
Status: Ready

````

## Requirements

- Create a function called `solution`.
- Accept two arguments:
  - `name` — student's name
  - `cohort` — student's cohort
- Use newline characters between each line.
- Do not add extra spaces or blank lines.
- Return the final string.

## Solution

```python
def solution(name, cohort):
    return f"Name: {name}\nCohort: {cohort}\nStatus: Ready"
````

## Example

```python
solution("Nuru", "Python Cohort 2026")
```

Output:

```
Name: Nuru
Cohort: Python Cohort 2026
Status: Ready
```

## Technologies Used

* Python 3