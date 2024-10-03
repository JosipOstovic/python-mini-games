#while loops

#value = 1
#while value < 10:
#    print(value)
#    if value == 5:
#        break
#    value += 1

value = 1
while value < 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("value is now equal to " + str(value))

#for loops
names = ["Josip","Mislav","Patrik"]
for x in names:
    print(x)

for x in "Josip":
    print(x)

for x in names:
    if x == "Mislav":
        break
    print(x)

#start u 0 do 50,inkrement je 5
for x in range(0,50,5):
    print(x)

actions = ["codes","eats","sleeps"]
for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
