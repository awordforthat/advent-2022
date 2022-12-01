with open("input.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

current_sum = 0
elves = []
for line in lines:
    if line == "":
        elves.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(line)
elves.append(current_sum)
print(sum(sorted(elves, reverse=True)[:3]))
