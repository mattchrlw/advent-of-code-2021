f = open('test/11.txt', 'r')
text = f.read()

def flash(grid, i, j, flashed):
    neighbours = [(i+1, j), (i+1, j-1), (i+1, j+1), \
        (i, j-1), (i, j+1), (i-1, j), (i-1, j+1), (i-1, j-1)]
    for n in neighbours:
        if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]):
            grid[n[0]][n[1]] += 1
            if grid[n[0]][n[1]] > 9 and (n[0], n[1]) not in flashed:
                flashed.append((n[0], n[1]))
                flash(grid, n[0], n[1], flashed)

def part1(text):
    grid = [[int(j) for j in i] for i in text.split("\n")]
    num_flashed = 0
    for iter in range(100):
        flashed = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
                if grid[i][j] > 9 and (i, j) not in flashed:
                    flashed.append((i, j))
                    flash(grid, i, j, flashed)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
        num_flashed += len(flashed)

    return num_flashed

def part2(text):
    grid = [[int(j) for j in i] for i in text.split("\n")]
    num_flashed = 0
    iter = 0
    while True:
        iter += 1
        flashed = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
                if grid[i][j] > 9 and (i, j) not in flashed:
                    flashed.append((i, j))
                    flash(grid, i, j, flashed)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
        num_flashed += len(flashed)
        all_zeros = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    all_zeros = False
        if all_zeros:
            break

    return iter

print(part1(text))
print(part2(text))