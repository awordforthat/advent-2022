with open("input.txt") as f:
    lines = [line.replace("\n", "").split(",") for line in f.readlines()]
    mid_sections = [(a.split("-"), b.split("-")) for a, b in lines]
    sections = [
        ((int(a[0]), int(a[1])), (int(b[0]), int(b[1]))) for a, b in mid_sections
    ]


def a():
    count = 0
    for a, b in sections:
        if a[0] >= b[0] and a[1] <= b[1] or b[0] >= a[0] and b[1] <= a[1]:
            count += 1
    print(count)


def b():
    count = 0
    for a, b in sections:
        a, b = sorted((a, b))
        count += 1 if b[0] <= a[1] else 0
    print(count)


a()
b()
