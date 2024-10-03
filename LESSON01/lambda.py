def squared(num): return num * num
#lambda num: num * num

print(squared(2))

def addTwo(num): return num + 2
#lambda num: num + 2

sum = lambda a, b : a + b
print(sum(2, 3))



####

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


#higher order functions

numbers = [2, 5, 11, 15, 4, 9]
squared_numbers = map(lambda num : num * num, numbers)

print(list(squared_numbers))

#filter

odd_numbers = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_numbers))

#####

from functools import reduce

numbers = [1,2,3,5,4,2,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)



names = ["Josip Ostovic","Mislav Ostovic", "Patrik Ostovic"]
char_count = reduce(lambda acc,curr: acc + len(curr), names, 0)
print(char_count)