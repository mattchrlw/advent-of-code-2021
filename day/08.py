from collections import defaultdict

f = open('test/08.txt', 'r')
text = f.read()

def part1(text):
    outputs = [i.split(" | ")[1] for i in text.split("\n")]
    letters = []
    output = 0
    for o in outputs:
        letters += o.split(" ")
    for l in letters:
        if len(l) in [2, 4, 3, 7]:
            output += 1
    return output

def part2(text):
    signals = [i.split(" | ")[0] for i in text.split("\n")]
    outputs = [i.split(" | ")[1] for i in text.split("\n")]
    nums = []
    for i in range(len(signals)):
        signs = signals[i].split(" ")
        d = {k: [] for k in [2,3,4,5,6,7]}
        for s in signs:
            d[len(s)].append(s)
        mappings = {}
        mappings['a'] = [i for i in d[3][0] if i not in d[2][0]][0]
        mappings['c'] = mappings['f'] = d[2][0]
        # 0, 6 and 9 have 6 segments each
        # f appears in 3, c only appears in 2
        for j in mappings['c']:
            if j in d[6][0] and j in d[6][1] and j in d[6][2]:
                mappings['f'] = j
            else:
                mappings['c'] = j
        # 2, 3 and 5 have 5 segments each
        # a, d and g are in common for all three
        # we already know a
        common = set(d[5][0]) & set(d[5][1]) & set(d[5][2])
        dg = common - set(mappings['a'])
        # d is the element of dg which is in the 4,
        # since 4 is the only one with 4 segments
        for j in dg:
            if j in d[4][0]:
                mappings['d'] = j
            else:
                mappings['g'] = j
        # finally, since we know c d and f,
        # we can figure out b since it is the only letter remaining in 4
        b = set(d[4][0]) - set(mappings['c'] + mappings['d'] + mappings['f'])
        mappings['b'] = next(iter(b))
        # mappings['e'] is just the only letter remaining
        mappings['e'] = next(iter(set('abcdefg') - set(mappings[i] for i in 'abcdfg')))
        # print(mappings)
        # need to invert mappings for convenience
        mappings = {v: k for k, v in mappings.items()}
        # now time to decode
        # turn outputs into decoded outputs
        decoded_outputs = []
        for o in outputs[i].split(" "):
            s = ""
            for j in o:
                s += mappings[j]
            decoded_outputs.append(''.join(sorted(s)))

        num = ""
        for o in decoded_outputs:
            if o == 'abcefg':
                num += '0'
            elif o == 'cf':
                num += '1'
            elif o == 'acdeg':
                num += '2'
            elif o == 'acdfg':
                num += '3'
            elif o == 'bcdf':
                num += '4'
            elif o == 'abdfg':
                num += '5'
            elif o == 'abdefg':
                num += '6'
            elif o == 'acf':
                num += '7'
            elif o == 'abcdefg':
                num += '8'
            elif o == 'abcdfg':
                num += '9'
        nums.append(int(num))
    return sum(nums)

print(part1(text))
print(part2(text))