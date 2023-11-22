from ex3.logic.logic import logic
from ex3.classes.player import Player
import random


def console_input():

    possibilities = ["rock", "paper", "scissors"]
    p = Player("", 0)
    c = Player("", 0)

    for i in range(3):
        opt = int(input("""
            Rock, Paper, Scissors?
            1 - Rock
            2 - Paper
            3 - Scissors
            input = """))

        logic(p, c, opt)

    if p.wins > c.wins:
        print("Player wins")
    if c.wins > p.wins:
        print("Computer wins")
    if p.wins == c.wins:
        print("It's a tie :(")
