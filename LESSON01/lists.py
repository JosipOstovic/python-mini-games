users = ['Josip','Patrik','Mislav']
data = ['Josip', 24, True]
emptyList = []
print("Josip" in users)
print(users[-1])

print(users.index('Mislav'))

print(users[0:2])
print(users[1:])

print(len(users))

users.append('Nikola')
users.append('Anita')
print(users)

users += ['Michael']
print(users)

users.extend(['John','Tim'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'Bober')
print(users)

users[2:2] = ['Miller','Alex']
print(users)

users[1:3] = ['Robert','Hulk']
print(users)

users.remove('Bober')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['josip']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [3,21,10,1,5]
nums.reverse()
print(nums)

#sortiranje silazno

# nums.sort(reverse=True)
# print(nums)

#sortiranje silazno ali zadržava originalnu listu
print(sorted(nums,reverse=True))
print(nums)

#kopija liste na više načina
numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]
print(numsCopy)
print(myNums)
myCopy.sort()
print(myCopy)
print(nums)

#kreiranje liste preko konstruktora
myList = list([1,2,"Josip",False])
print(myList)

#Tuples
myTuple = tuple(('Josip',24,True))
anotherTuple = (1,2,3)
print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append('Jozex')
newTuple = tuple(newList)
print(newTuple)

(jedan,*dva,hey) = anotherTuple
print(jedan)
print(dva)
print(hey)

print(anotherTuple.count(2))

