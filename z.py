import math

def calculate_tuple_product(tup):
    
    return math.prod(tup)


tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)


print(f"The product of tup1 is: {calculate_tuple_product(tup1)}")
print(f"The product of tup2 is: {calculate_tuple_product(tup2)}")