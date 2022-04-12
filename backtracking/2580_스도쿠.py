import sys

grid = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]


def get_num(x, y):
    items = []

    for i in range(9):
        items.append(grid[x][i])
        items.append(grid[i][y])

    sqx, sqy = x // 3, y // 3
    for i in range(sqx * 3, (sqx + 1) * 3):
        for j in range(sqy * 3, (sqy + 1) * 3):
            items.append(grid[i][j])

    return set(range(1, 10)) - set(items)


def solve(k):
    if k == len(zeros):
        for i in grid:
            print(*i)
        sys.exit()

    x, y = zeros[k]
    for j in get_num(x, y):
        grid[x][y] = j
        solve(k + 1)
        grid[x][y] = 0


solve(0)
