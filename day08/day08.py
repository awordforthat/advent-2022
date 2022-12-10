with open("input.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

grid = [[int(ch) for ch in line] for line in lines]


def a():
    visible_pts = set()

    for i in range(len(grid)):
        max_to_left = -1
        for j in range(len(grid[i])):
            if max_to_left < grid[i][j]:
                visible_pts.add((i, j))
            max_to_left = max(max_to_left, grid[i][j])

        max_to_right = -1
        for j in range(len(grid[i]) - 1, -1, -1):
            if max_to_right < grid[i][j]:
                visible_pts.add((i, j))
            max_to_right = max(max_to_right, grid[i][j])

    for i in range(len(grid[0])):
        col = [row[i] for row in grid]
        max_to_top = -1
        for j in range(len(col)):
            if max_to_top < grid[j][i]:
                visible_pts.add((j, i))
            max_to_top = max(max_to_top, grid[j][i])
        max_to_bottom = -1
        for j in range(len(col) - 1, -1, -1):
            if max_to_bottom < grid[j][i]:
                visible_pts.add((j, i))
            max_to_bottom = max(max_to_bottom, grid[j][i])

    print(len(visible_pts))


def get_visibility(line, val, reversed=False):
    count = 0

    for pointer in range(len(line) - 1, -1, -1) if reversed else (range(len(line))):
        count += 1
        if line[pointer] >= val:
            break
    return count


def b():
    scores = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = grid[i][j]
            left_visibility = get_visibility(grid[i][:j], value, True)
            right_visibilty = get_visibility(grid[i][j + 1 :], value)
            column = [grid[row][j] for row in range(len(grid))]
            top_visibility = get_visibility(column[:i], value, True)
            bottom_visibility = get_visibility(column[i + 1 :], value)
            scores[i, j] = (
                left_visibility * right_visibilty * top_visibility * bottom_visibility
            )

    max_score = -1
    for point in scores:
        max_score = max(max_score, scores[point])

    print(max_score)


a()
b()
