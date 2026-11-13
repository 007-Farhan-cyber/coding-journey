def countdown(number):
    print(number)

    if number>1:
        countdown(number-1)
countdown(5)

#2

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))

#3

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)

print(sum_to_n(5))