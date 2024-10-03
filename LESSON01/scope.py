name = "Josip"
count = 1

def greeting(fName):
    color = "red"
    global count
    count += 1
    print(count)
    print(color)
    print(name)
    print(fName)

greeting("Mislav")

def another():
    greeting("Paki")

another()