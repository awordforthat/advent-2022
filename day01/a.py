with open("input.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

# print(lines)

maximum = 0
sum = 0
for line in lines:
    if line == "":
        maximum = max(maximum, sum)
        sum = 0
    else:
        sum += int(line)
print(maximum)
