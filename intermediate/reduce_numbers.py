#using lambda functions and HOF(reduce)

#Import reduce
from functools import reduce

my_list = [2,2,2,2,2]
reduction = reduce(lambda a,b:a*b, my_list)
print(reduction)