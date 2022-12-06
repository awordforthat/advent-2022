with open("input.txt") as f:
    lines = [line for line in f.readlines()]

stack_depth = 0
for line in lines:
    if line == "\n":
        break
    stack_depth += 1


instructions = [line.replace("\n", "") for line in lines[stack_depth + 1 :]]


def setup():
    stack = [line.replace("\n", "") for line in lines[:stack_depth]]
    num_stacks = len(stack[-1].replace(" ", ""))
    stacks = []
    for i in range(num_stacks):
        stacks.append([])

    stack_width = 4
    for level in list(reversed(stack))[1:]:
        for i in range(0, len(level), stack_width):
            package = level[i + 1]
            if package == " ":
                continue
            stacks[i // stack_width].append(level[i + 1])
    return stacks, num_stacks


def print_answer(stacks, num_stacks):
    for i in range(num_stacks):
        print(stacks[i][-1], end="")
    print()


def a():
    stacks, num_stacks = setup()
    for instruction in instructions:
        _move, num_to_move, _from, from_stack, _to, to_stack = instruction.split(" ")
        for i in range(int(num_to_move)):
            stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())
    print_answer(stacks, num_stacks)


def b():
    stacks, num_stacks = setup()
    for instruction in instructions:
        _move, num_to_move, _from, from_stack, _to, to_stack = instruction.split(" ")
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        num_to_move = int(num_to_move)
        moving = stacks[from_stack][-num_to_move:]
        stacks[to_stack] = stacks[to_stack] + moving
        stacks[from_stack] = stacks[from_stack][
            0 : len(stacks[from_stack]) - num_to_move
        ]
    print_answer(stacks, num_stacks)


a()
b()
