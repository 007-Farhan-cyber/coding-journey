numbers = (12, 7, 18, 5, 24, 9, 30)

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

count = 0

for num in numbers:
    result = check_even_odd(num)

    if result == "Odd":
        print(num)
        count = count + 1

print("Total odd numbers:", count)