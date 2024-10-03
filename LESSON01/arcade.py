import sys
from rockpaper import rps
from guess_number import guess_number

def play_game(name='Some Player'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerChoice = input("\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\n Or press \"x\" to exit the Arcade \n\n")

        if playerChoice not in ["1","2","x"]:
            print(f"\n{name}, please enter 1, 2 or x.")
            return play_game(name)
        
        welcome_back = True

        if playerChoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerChoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("See you next time!\n")
            sys.exit(f"Bye {name}!")
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The of the person playing the game'
    )

    args = parser.parse_args()
    print(f"\n{args.name}, welcome to the Arcade!")
    
    play_game(args.name)