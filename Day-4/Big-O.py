    #Big O Basics covered 
    #Differnce between O(1), O(n) and O(n²)
    #List Slicing  is jumping between O(1) and O(n) depending on the size of the slice

numbers = [5, 10, 15, 20, 25, 30, 35, 40]
print(numbers[0:4])
print(numbers[5:])
print(numbers[0:1])  # This will print the first element
print(numbers[2:3])  # This will print the third element
print(numbers[4:5])  # This will print the fifth element
print(numbers[2:5])
print(numbers[::-1])
