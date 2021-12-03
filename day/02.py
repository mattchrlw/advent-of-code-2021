f = open('test/02.txt', 'r')
text = f.read()

def part1(text):
    lines = text.split("\n")
    x, y = 0, 0
    for l in lines:
        direction, dist = l.split()
        dist = int(dist)
        if direction == "forward":
            x += dist
        elif direction == "up":
            y -= dist
        elif direction == "down":
            y += dist
    return x * y

def part2(text):
    lines = text.split("\n")
    x, y, aim = 0, 0, 0
    for l in lines:
        direction, dist = l.split()
        dist = int(dist)
        if direction == "forward":
            x += dist
            y += dist * aim
        elif direction == "up":
            aim -= dist
        elif direction == "down":
            aim += dist
    return x * y

print(part1(text))
print(part2(text))