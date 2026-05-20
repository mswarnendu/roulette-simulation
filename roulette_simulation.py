import random
import matplotlib.pyplot as plt
import numpy as np

"""
Convergence Test of European Style Roulette

Setup:
    - There are 37 possible pockets, with numbers between 0-36 (inclusive)
    - Every number can be a color red, green, or black

Inputs:
    - Betting number: what number you want to bet on every game

Outputs:
    - House Advantage: How much advantage the house (opposing player) has in the roulette game.
    - Convergence Graph: Shows how the probability of a win evolves over an increased sample size.

"""


def main():

    BET = int(input("Input what number you always want to bet on: "))
    TRIALS = 1_000_000
    STEPS = 1_000
    wins = 0
    prob_y = []

    for trial in range(1, TRIALS + 1):
        actual = random.randint(0, 36)

        if actual == BET:
            wins += 1

        if trial % STEPS == 0:
            prob_y.append(wins / trial)

        win_prob = wins / TRIALS
        loss_prob = 1 - win_prob

    prob_x = np.linspace(0, TRIALS, 1000)

    EV = 35 * win_prob - 1 * loss_prob
    house_advantage = -EV * 100

    plt.plot(prob_x, prob_y)
    plt.grid(True)
    plt.title(
        f"Convergence Test of European Style Roulette Wheel with Betting on {BET} Everytime")
    plt.xlabel("Games Ran")
    plt.ylabel("Estimated Probability")
    plt.show()

    print("ROULETTE METRICS\n")
    print(f"Win Probability: {(win_prob * 100):.3f}%")
    print(f"House Advantage {(house_advantage):.3f}%")


if __name__ == "__main__":
    main()
