f = open('test/05.txt', 'r')
text = f.read()

def part1(text):
    points = [i.split(" -> ") for i in text.split("\n")]
    mapp = [[0] * 1000 for i in range(1000)]
    for p in points:
        a = [int(j) for j in p[0].split(",")]
        b = [int(j) for j in p[1].split(",")]
        if a[0] == b[0]:
            ys = sorted([a[1], b[1]])
            for y in range(ys[0], ys[1] + 1):
                mapp[a[0]][y] += 1
        elif a[1] == b[1]:
            xs = sorted([a[0], b[0]])
            for x in range(xs[0], xs[1] + 1):
                mapp[x][a[1]] += 1
    return (len([i for j in mapp for i in j if i >= 2]))

def part2(text):
    points = [i.split(" -> ") for i in text.split("\n")]
    mapp = [[0] * 1000 for i in range(1000)]
    for p in points:
        a = [int(j) for j in p[0].split(",")]
        b = [int(j) for j in p[1].split(",")]
        if a[0] == b[0]:
            ys = sorted([a[1], b[1]])
            for y in range(ys[0], ys[1] + 1):
                mapp[a[0]][y] += 1
        elif a[1] == b[1]:
            xs = sorted([a[0], b[0]])
            for x in range(xs[0], xs[1] + 1):
                mapp[x][a[1]] += 1
        elif abs(b[0] - a[0]) == abs(b[1] - a[1]):
            x, y = a[0], a[1]
            mapp[x][y] += 1
            x_dir = 1 if a[0] <= b[0] else -1
            y_dir = 1 if a[1] <= b[1] else -1
            while x != b[0] and y != b[1]:
                x += x_dir
                y += y_dir
                mapp[x][y] += 1
                
    return (len([i for j in mapp for i in j if i >= 2]))

print(part1(text))
print(part2(text))