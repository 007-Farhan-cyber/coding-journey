numbers = [2, 4, 6, 8, 10, 12, 14]
target = 8

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found at index:", middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1