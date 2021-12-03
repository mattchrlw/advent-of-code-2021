f = open('test/01.txt', 'r')
text = f.read()

def part1(text):
    nums = [int(i) for i in text.split()]
    increases = 0
    for idx, i in enumerate(nums):
        if idx == 0:
            pass
        else:
            if nums[idx-1] < i:
                increases += 1

    return increases

def part2(text):
    nums = [int(i) for i in text.split()]
    increases = 0
    for idx in range(len(nums)):
        if idx < 3:
            pass
        else:
            if sum(nums[idx-3:idx]) < sum(nums[idx-2:idx+1]):
                increases += 1

    return increases

print(part1(text))
print(part2(text))