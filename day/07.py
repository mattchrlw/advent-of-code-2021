f = open('test/07.txt', 'r')
text = f.read()

def part1(text):
    l = [int(i) for i in text.split(",")]
    lowest = float('inf')
    for align in range(max(l)):
        new_l = sum([abs(align - k) for k in l])
        if new_l < lowest:
            lowest = new_l
    return lowest

def part2(text):
    l = [int(i) for i in text.split(",")]
    lowest = float('inf')
    for align in range(max(l)):
        new_l = sum([abs(align - k)*(abs(align - k) + 1)//2 for k in l])
        if new_l < lowest:
            lowest = new_l
    return lowest

print(part1(text))
print(part2(text))