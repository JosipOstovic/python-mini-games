import sys
import random

def guess_number(name="Some Player"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerChoice = input(f"\n{name}, guess which number I'm thinking of from 1 to 9...\n\n")
        
        if playerChoice not in ["1","2","3","4","5","6","7","8","9"]:
            print(f"{name}, please enter a number from 1 to 10:")
            return play_guess_number()
        
        computerChoice = random.choice("123456789")
        print(f"\n{name}, you chose {playerChoice}")
        print(f"\nI was thinking about the number {computerChoice}.\n")

        player = int(playerChoice)
        computer = int(computerChoice)

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time"
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")
        print(f"\nPlay again, {name}?")

        while True:
            playAgain = input("\nY for Yes or \nQ to Quit\n")
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return play_guess_number()
        else:
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return
    
    return play_guess_number

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized game experience")
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()