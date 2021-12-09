f = open('test/09.txt', 'r')
text = f.read()

def part1(text):
    grid = text.split("\n")
    m = []
    lows = []
    for g in grid:
        m.append([int(i) for i in g])
    for i in range(len(m)):
        for j in range(len(m[0])):
            w = m[i-1][j] if i > 0 else float('inf')
            e = m[i+1][j] if i < len(m) - 1 else float('inf')
            n = m[i][j-1] if j > 0 else float('inf')
            s = m[i][j+1] if j < len(m[0]) - 1 else float('inf')
            if m[i][j] < n and m[i][j] < s \
                and m[i][j] < w and m[i][j] < e:
                lows.append(m[i][j] + 1)
    return sum(lows)

def helper(m, i, j, visited):
    neighbours = [(m[i+k[0]][j+k[1]], i+k[0], j+k[1]) for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if i+k[0] >= 0 and i+k[0] < len(m) and j+k[1] >= 0 and j+k[1] < len(m[0])]
    new_neighbours = [n for n in neighbours if n[0] == 0 and (n[1], n[2]) not in visited]
    if len(new_neighbours) == 0:
        return 0, visited
    else:
        visited += [(n[1], n[2]) for n in new_neighbours]
        return len(new_neighbours) + sum(helper(m, n[1], n[2], visited)[0] for n in new_neighbours), visited

def part2(text):
    grid = text.split("\n")
    m = []
    for g in grid:
        m.append([9 if i == '9' else 0 for i in g])
    basins = []
    visited = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0 and (i, j) not in visited:
                basin, new_visited = helper(m, i, j, [(i, j)])
                basins.append(basin + 1)
                visited += new_visited
    sorted_basins = sorted(basins, reverse=True)
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]

print(part1(text))
print(part2(text))