import random
from ex3.output.output import show_signs


def logic(p, c, opt):
    possibilities = ["rock", "paper", "scissors"]
    if opt == 1:
        p.choice = "rock"
        c.choice = random.choice(possibilities)
    if opt == 2:
        p.choice = "paper"
        c.choice = random.choice(possibilities)
    if opt == 3:
        p.choice = "scissors"
        c.choice = random.choice(possibilities)

    show_signs(p, c)

    if p.choice == "scissors":
        if c.choice == "rock":
            print("The computer took a point")
            c.wins += 1
        if c.choice == "paper":
            p.wins += 1
            print("The player took a point")

    if p.choice == "paper":
        if c.choice == "rock":
            p.wins += 1
            print("The player took a point")
        if c.choice == "scissors":
            c.wins += 1
            print("The computer took a point")

    if p.choice == "rock":
        if c.choice == "paper":
            c.wins += 1
            print("The computer took a point")
        if c.choice == "scissors":
            p.wins += 1
            print("The player took a point")

    print(f"The current score is Player: {p.wins} and Computer: {c.wins}")
