s = "anagram"
t = "nagaram"

count_s = {}
count_t = {}
for letter in s:
    if letter in count_s:
        count_s[letter] += 1
    else:
        count_s[letter] = 1

for letter in t:
    if letter in count_t:
        count_t[letter] += 1
    else:
        count_t[letter] = 1

print(count_s)
print(count_t)