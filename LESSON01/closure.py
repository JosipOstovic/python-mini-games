def parent_function(person,coins):
    #coins = 5

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left")
        else:
            print("\n" + person + " is out of coins")

    return play_game

josip = parent_function("Josip", 4)
patrik = parent_function("Patrik", 3)

josip()
josip()
josip()
josip()

patrik()