from random import choice

capital = "Zagreb"
flower = "Jaglac"
bird = "Roda"
song = "Lijepa Naša"

def randomfunFact():
    funFacts = [
        "Croatia is the most beautiful country in the world with a national parks and beautiful islands.",
        "Zagreb is the capital and the largest city and it has more population than the next 4 biggest cities together.",
        "Croatia has more than 1000 islands and one of them is in top 10 most beautiful islands in the world.",
        "In the last 5 years, more than 250 000 people left Croatia for better life."
    ]

    index = choice("0123")
    print(funFacts[int(index)])

if __name__ == "__main__":
    randomfunFact()