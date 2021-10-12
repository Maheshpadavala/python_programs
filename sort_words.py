# Program to sort words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)