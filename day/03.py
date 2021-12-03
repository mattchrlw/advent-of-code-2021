from collections import defaultdict

f = open('test/03.txt', 'r')
text = f.read()

def part1(text):
    lines = text.split("\n")
    counts = defaultdict(lambda: 0)
    for l in lines:
        for idx, k in enumerate(l):
            if k == '1':
                counts[idx] += 1

    epsilon = ''
    gamma = ''
    for i in range(len(lines[0])):
        if counts[i] > len(lines)/2:
            epsilon += '1'
            gamma += '0'
        else:
            epsilon += '0'
            gamma += '1'

    return (int(epsilon, 2) * int(gamma,2))
    

def part2(text):
    lines = text.split("\n")
    idxs = len(lines[0])
    i = 0
    nums = lines
    while i < idxs:
        zeros = [n[i] for n in nums if n[i] == '0']
        ones = [n[i] for n in nums if n[i] == '1']
        if len(zeros) > len(ones):
            nums = list(filter(lambda x: x[i] == '0', nums))
        else:
            nums = list(filter(lambda x: x[i] == '1', nums))
        if len(nums) == 1:
            break
        i += 1
    oxygen = int(nums[0], 2)
    i = 0
    nums = lines
    co2 = ""
    while i < idxs:
        zeros = [n[i] for n in nums if n[i] == '0']
        ones = [n[i] for n in nums if n[i] == '1']
        if len(zeros) > len(ones):
            nums = list(filter(lambda x: x[i] == '1', nums))
        else:
            nums = list(filter(lambda x: x[i] == '0', nums))
        if len(nums) == 1:
            break
        i += 1
    co2 = int(nums[0], 2)
    return (oxygen * co2)
    

print(part1(text))
print(part2(text))