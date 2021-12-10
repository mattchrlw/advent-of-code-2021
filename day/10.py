from collections import defaultdict

f = open('test/10.txt', 'r')
text = f.read()

def part1(text):
    rtl = {")": "(", "]": "[", "}": "{", ">": "<"}
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupted = []
    lines = text.split("\n")
    for l in lines:
        punctuation = []
        for c in l:
            if c in ["(", "[", "{", "<"]:
                punctuation.append(c)
            else:
                if rtl[c] == punctuation[-1]:
                    punctuation.pop()
                else:
                    corrupted.append(c)
                    break
    score = 0
    for c in corrupted:
        score += values[c]
    return score

def part2(text):
    rtl = {")": "(", "]": "[", "}": "{", ">": "<"}
    ltr = {v:k for k, v in rtl.items()}
    values = {")": 1, "]": 2, "}": 3, ">": 4}
    corrupted = []
    lines = text.split("\n")
    for l in lines:
        punctuation = []
        for c in l:
            if c in ["(", "[", "{", "<"]:
                punctuation.append(c)
            else:
                if rtl[c] == punctuation[-1]:
                    punctuation.pop()
                else:
                    corrupted.append(l)
    lines = [l for l in lines if l not in corrupted]
    scores = []
    for l in lines:
        punctuation = []
        for c in l:
            if c in ["(", "[", "{", "<"]:
                punctuation.append(c)
            else:
                if rtl[c] == punctuation[-1]:
                    punctuation.pop()
        new_scores = [values[ltr[i]] for i in list(reversed(punctuation))]
        new_score = 0
        for n in new_scores:
            new_score = 5 * new_score + n
        scores.append(new_score)
    return sorted(scores)[len(scores) // 2]

print(part1(text))
print(part2(text))