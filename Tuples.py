#Tuples look almost identical, except they use round brackets () instead of square brackets [].
#tuples are immutable, meaning you cannot replace, add or remove their elements after creation.
numbers = (5, 10, 15, 10, 20, 25, 10)
print(numbers[0])
print(numbers[-1])
print(len(numbers))
print(numbers.count(10))
print(numbers.index(20))
print(numbers[::-1])