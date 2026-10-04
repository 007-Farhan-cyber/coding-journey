numbers = [2, 5, 2, 7, 5, 2, 9, 7]
counts = {}
for number in numbers:
    if number in counts:
        counts[number] = counts[number] + 1
    else:
        counts[number] = 1

print(counts)


#2
numbers = numbers = [4, 8, 4, 3, 8, 8, 2, 3, 4]
counts = {}
for number in numbers:
    if number in counts:
        counts[number] = counts[number] + 1
    else:
        counts[number] = 1

print(counts)
