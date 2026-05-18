#evens = list(filter(lambda x: x % 2 == 0, nums))

data = [1,2,3,4,5,6,7,8,9]

square = list(map(lambda data : data**2,data))
print(f"square :{square}")
evens = list(filter(lambda x: x % 2 == 0, data))
print(f"even:{evens}")
odd = list(filter(lambda x: x % 2 != 0, data))
print(f"even:{odd}")
from functools import reduce
addition = reduce(lambda x , y :x+y , data)
print(f"Addition is. :{addition}")
maximum = reduce(lambda x , y : max(x , y ) ,data)
print(f"max  nos : {maximum}")


