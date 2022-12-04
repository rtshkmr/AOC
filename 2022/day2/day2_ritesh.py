#!/usr/bin/env python3
"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

"""

def parse_input(url, readlines=False):
    """
    Parses input file via provided url.
    Returns lines read as a list if readlines is True.
    """

    try:
        with open(url, 'r') as file:
            content = file.readlines() if readlines else file.read()

            return content

    except Exception as e:
        msg = f"Error reading input file: {e}"
        print(msg)

    return None

def flip_choice(choice, negate=False, win=False):
    """
    [A, B, C]

    [X, Y, Z]

    rock beats scissor
    A beats C
    X beats Z

    paper beats rock
    B beats A
    Y beats X

    scissor beats paper
    C beats B
    Z beats Y
    """

    # easy enough to just write multiple if statements
    if choice == "X":
        if not negate: return "A"
        return "C" if win else "B"

    if choice == 'A':
        if not negate: return "X"
        return "Z" if win else "Y"

    if choice == "Y":
        if not negate: return "B"
        return "A" if win else "C"

    if choice == 'B':
        if not negate: return "Y"
        return "X" if win else "Z"

    if choice == "Z":
        if not negate: return "C"
        return "B" if win else "A"

    if choice == 'C':
        if not negate: return "Z"
        return "Y" if win else "X"

    return

def get_round_outcome(opp_choice, my_choice):
    if opp_choice == flip_choice(my_choice):
        return 3

    # win outcomes:
    if (
            (opp_choice == 'A' and my_choice == 'Y') or
            (opp_choice == 'B' and my_choice == 'Z') or
            (opp_choice == 'C' and my_choice == 'X')
    ):
        return 6

    # loss outcome
    return 0

def get_choice_score(choice):
    if choice == 'A' or choice == 'X':
        return 1

    if choice == 'B' or choice == 'Y':
        return 2

    if choice == 'C' or choice == 'Z':
        return 3

    return None

def solve_part_1(input_lines):

    my_score = 0

    for round_line in input_lines:
        opp_choice, my_choice = choices = round_line.strip().split(' ')
        round_outcome = get_round_outcome(opp_choice, my_choice)
        choice_score = get_choice_score(my_choice)

        score = round_outcome + choice_score

        my_score += score

    return my_score


def get_score_from_outcome(outcome, opp_choice):
    outcome_score = 0
    choice_score = 0

    if outcome == 'Y':
        # draw
        outcome_score = 3
        my_choice = flip_choice(opp_choice)
        choice_score = get_choice_score(my_choice)

    if outcome == 'Z':
        # you win, opp loses
        outcome_score = 6
        my_choice = flip_choice(opp_choice, negate=True, win=False)
        choice_score = get_choice_score(my_choice)

    if outcome == 'X':
        # you lose, opp wins
        outcome_score = 0
        my_choice = flip_choice(opp_choice, negate=True, win=True)
        choice_score = get_choice_score(my_choice)

    return outcome_score + choice_score

def solve_part_2(input_lines):
    my_score = 0

    for round_line in input_lines:
        opp_choice, eventual_outcome = round_line.strip().split(' ')
        score = get_score_from_outcome(eventual_outcome, opp_choice)
        my_score += score

    return my_score

def main():
    input_lines = parse_input('./input.in', readlines=True)

    if not input_lines:
        msg = "Why even bother!?"
        print(msg)

        return

    part_1_solution = solve_part_1(input_lines)
    part_2_solution = solve_part_2(input_lines)

    print(f"part 1 solution: {part_1_solution} ")
    print(f"part 2 solution: {part_2_solution} ")

    return

if __name__ == "__main__":
    main()
