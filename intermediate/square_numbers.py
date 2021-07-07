#using lambda functions and HOF(map)
my_list = [1,2,3,4,5]
square = list(map(lambda x:x**2, my_list))
print(square)