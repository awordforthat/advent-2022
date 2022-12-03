with open("input.txt") as f:
    rounds = [
        line.split(" ") for line in [line.replace("\n", "") for line in f.readlines()]
    ]

moves = "ABCXYZ"
scores = {0: 3, 1: 6, 2: 0}
outcomes = {"X": 2, "Y": 0, "Z": 1}


def score_round(my_index, opponent_move):
    return (my_index % 3) + 1 + scores[(my_index - moves.index(opponent_move)) % 3]


def a():

    score = 0
    for opponent_move, my_move in rounds:
        my_index = moves.index(my_move)
        score += score_round(my_index, opponent_move)
    print(score)


def b():
    score = 0
    for opponent_move, goal in rounds:
        score += score_round(
            (moves.index(opponent_move) + outcomes[goal]) % 3 + 3, opponent_move
        )
    print(score)


a()
b()
