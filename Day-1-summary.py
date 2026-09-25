number = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(number)
print(f"The number {number} is {result}.")

for i in range(1, number + 1):
    print(i)