with open("input.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]


def score_letter(letter):
    is_lower = letter.lower() == letter
    return ord(letter) - (97 if is_lower else 65) + (1 if is_lower else 27)


def a():
    rucksacks = [
        (line[0 : (len(line) // 2)], line[(len(line) // 2) :]) for line in lines
    ]
    score = 0
    for left, right in rucksacks:
        score += score_letter((set(left) & set(right)).pop())
    print(score)


def b():
    score = 0
    for i in range(0, len(lines) - 1, 3):
        score += score_letter(
            (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
        )
    print(score)


a()
b()
