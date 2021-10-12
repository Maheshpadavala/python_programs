input_string = "mahesh"

vowels = "aeiou"

count = {}.fromkeys(vowels, 0)

for char in input_string:
    if char in vowels:
        count[char] += 1

print(count)
