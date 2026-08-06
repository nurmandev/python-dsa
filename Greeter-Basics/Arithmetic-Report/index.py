def solution(name, a, b, c):
    total = a + b + c
    average = round(total / 3, 2)
    maximum = max(a, b, c)

    return f"Student: {name}\nSum: {total}\nAverage: {average:.2f}\nMaximum: {maximum}"