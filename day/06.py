f = open('test/06.txt', 'r')
text = f.read()

def part1(text):
    l = [int(i) for i in text.split(",")]
    for _ in range(80):
        new_l = []
        num_8s = 0
        for j in l:
            k = j-1
            if k == -1:
                new_l.append(6)
                num_8s += 1
            else:
                new_l.append(k)
        new_l += [8] * num_8s
        l = new_l
    return len(l)

def part2(text):
    l = [int(i) for i in text.split(",")]
    nums = {k: l.count(k) for k in range(9)}
    for _ in range(256):
        new_nums = {k-1: v for k, v in nums.items()}
        new_nums[6] += new_nums[-1]
        new_nums[8] = new_nums[-1]
        nums = {k: v for k, v in new_nums.items() if k >= 0}
    return sum(nums.values())

print(part1(text))
print(part2(text))