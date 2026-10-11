#Palindrome using two pointers
word = "2022"

left = 0
right = len(word) - 1

while left < right:
    if word[left] != word[right]:
        print("Not palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
