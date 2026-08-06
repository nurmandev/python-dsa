# Arithmetic Report

## Description

This project contains a simple Python function that generates a student's arithmetic report using a student's name and three numbers.

The report includes:

- Student name
- Sum of the three numbers
- Average rounded to 2 decimal places
- Maximum value among the numbers

## Output Format

```

Student: [name]
Sum: [sum]
Average: [average]
Maximum: [maximum]

````

## Requirements

- Create a function called `solution`.
- Accept four arguments:
  - `name` — student's name
  - Three numbers for calculation
- Calculate the sum of the numbers.
- Calculate the average and round it to 2 decimal places.
- Find the largest number.
- Return the final multi-line string.
- Do not print the output.

## Solution

```python
def solution(name, a, b, c):
    total = a + b + c
    average = round(total / 3, 2)
    maximum = max(a, b, c)

    return f"Student: {name}\nSum: {total}\nAverage: {average:.2f}\nMaximum: {maximum}"
````

## Example

```python
solution("Nuru", 10, 20, 30)
```

Output:

```
Student: Nuru
Sum: 60
Average: 20.00
Maximum: 30
```

## Technologies Used

* Python 3