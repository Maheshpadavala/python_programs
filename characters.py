input_string = "maheshmaheahmahesh"

count = {}

for char in input_string:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

print(count)
