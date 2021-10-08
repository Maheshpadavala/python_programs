# Take a list of numbers
my_list = [5, 58, 65, 87, 120, 553, 1005]

# use anonymous function to filter
result = list(filter(lambda x: (x % 5 == 0), my_list))

# display the result
print("Numbers divisible by 5 are",result)