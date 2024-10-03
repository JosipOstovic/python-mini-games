person = "Josip"
coins = 3

#korištenje %s (stariji pristup)
message = "\n%s has %s coins left." % (person,coins)
print(message)

#format method
message = "\n{} has {} coins left.".format(person,coins)
print(message)

#još jedan način
message = "\n{1} has {0} coins left.".format(coins,person)
print(message)

#još jedan način
message = "\n{person} has {coins} coins left.".format(coins=coins,person=person)
print(message)



player = { 'person': 'Josip', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)


#f-strings
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {3*7} coins left."
print(message)

message = f"\n{person.lower()} has {coins} coins left."
print(message)

message = f"\n{player['person']} has {coins} coins left."
print(message)

#formatting options
num = 10
print(f"\n3.5 times {num} is {3.5 * num:.2f}\n")

for num in range(1,11):
    print(f"3.5 times {num} is {3.5 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 3.14 is {num / 3.14:.2%}")

