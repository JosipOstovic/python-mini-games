#Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

secondBand = dict(vocals="Plant", guitar="Page")

print(band)
print(secondBand)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("circle" in band)

#change values
band["vocals"] = "Netko"
band.update({"bass": "Neil"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Jozex"
print(band)

print(band.popitem()) # returns as tuple
print(band)

#delete and clear
band["drums"] = "Jozex"
del band["drums"]
print(band)

secondBand.clear()
print(secondBand)
del secondBand

#copy dictionaries -> ovo ispod je loš način
secondBand = band # create a reference
print("Bad copy!")
print(secondBand)
print(band)

secondBand["drums"] = "Josip"
print(band)

#dobar način
secondBand = band.copy()
secondBand["drums"] = "Josip"
print("Good copy!")
print(secondBand)

#copy with dict() constructor function
thirdBand = dict(band)
print("Good copy!")
print(thirdBand)

#Nested dictionaries
firstMember = {
    "name": "Plant",
    "instrument": "vocals"
}
secondMember = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "firstMember": firstMember,
    "secondMember": secondMember,
}
print(band)
print(band["firstMember"]["name"])

#Sets
nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicate allowed
nums = {1,2,2,3}
print(nums)

#True is a dupe of 1, False is a dupe of zero
nums = {1,True,2,False,3,4,0}
print(nums)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#add a new element to a set
nums.add(8)
print(nums)

#add elements from one set to another
moreNums = {7,8,9}
nums.update(moreNums)
print(nums)

#you can use update() with lists,tuples and dictionaries too

#merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}
myNewSet = one.union(two)
print(myNewSet)

#Keep only the duplicates
one = {1,2,3}
two = {2,3,7}
one.intersection_update(two)
print(one)

#Keep everything except the duplicates
one = {1,2,3}
two = {2,3,7}
one.symmetric_difference_update(two)
print(one)