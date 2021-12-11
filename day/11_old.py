from pprint import pprint

f = open('test/11.txt', 'r')
text = f.read()

def flash(grid, i, j, flashes):
    grid[i][j] = 0
    neighbours = [(i, j-1), (i, j+1), (i-1, j-1), (i-1, j),\
            (i-1, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    flashes = []
    for n in neighbours:
        if 0 < n[0] < len(grid) and 0 < n[1] < len(grid[0]):
            grid[n[0]][n[1]] += 1
            if grid[n[0]][n[1]] > 9 and (n[0], n[1]) not in flashes:
                flashes.append((n[0], n[1]))
    if len(flashes) > 0:
        return 1 + len(flashes) + sum(flash(grid, i[0], i[1], flashes) for i in flashes)
    else:
        return 0

def part1(text):
    grid = [list([int(j) for j in i]) for i in text.split("\n")]
    pprint(grid)
    total_flashes = 0
    for iter in range(100):
        flashes = []
        # increase by 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
        # initiate flashes
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    flashes.append((i, j))
        for f in flashes:
            num_flashes = flash(grid, f[0], f[1], flashes)
            total_flashes += num_flashes
        print("Step", iter+1)
        pprint(grid)
    print(total_flashes)

def part2(text):
    pass

print(part1(text))
print(part2(text))