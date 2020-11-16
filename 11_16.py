from functools import reduce

#1.map
def function1(list):
    list = list[0].upper() + list[1:].lower()
    return list
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(function1, L1))
print(L2)

#2.prod
def prod(list):
    return reduce(lambda x, y: x*y,list)
L3 = [1,2,3,4]
print(prod(L3))
