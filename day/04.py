import numpy as np

f = open('test/04.txt', 'r')
text = f.read()

def part1(text):
    data = text.split("\n\n")
    numbers = [int(i) for i in data[0].split(",")]
    boards = data[1:]
    boards_formatted = []
    for b in boards:
        rows = [[int(j) for j in i.split()] for i in b.split("\n")]
        boards_formatted.append(np.array(rows))
    boards = boards_formatted
    for n in numbers:
        for idx, b in enumerate(boards):
            b = np.where(b == n, -1, b)
            boards[idx] = b
            rows = [sum(boards[idx][:,i]) for i in range(5)]
            cols = [sum(boards[idx][i,:]) for i in range(5)]
            for r in rows:
                if r == -5:
                    unmarked = sum([elem for k in boards[idx] for elem in k  if elem != -1])
                    called = n
                    return unmarked * called
            for c in cols:
                if c == -5:
                    unmarked = sum([elem for k in boards[idx] for elem in k  if elem != -1])
                    called = n
                    return unmarked * called

def part2(text):
    data = text.split("\n\n")
    numbers = [int(i) for i in data[0].split(",")]
    boards = data[1:]
    boards_formatted = []
    for b in boards:
        rows = [[int(j) for j in i.split()] for i in b.split("\n")]
        boards_formatted.append(np.array(rows))
    boards = boards_formatted
    seen_indices = set()
    for n in numbers:
        for idx, b in enumerate(boards):
            if idx not in seen_indices:
                b = np.where(b == n, -1, b)
                boards[idx] = b
                rows = [sum(boards[idx][:,i]) for i in range(5)]
                cols = [sum(boards[idx][i,:]) for i in range(5)]
                for r in rows:
                    if r == -5:
                        if len(seen_indices) == len(boards) - 1:
                            unmarked = sum([elem for k in boards[idx] for elem in k  if elem != -1])
                            called = n
                            return unmarked * called
                        seen_indices.add(idx)
                for c in cols:
                    if c == -5:
                        if len(seen_indices) == len(boards) - 1:
                            unmarked = sum([elem for k in boards[idx] for elem in k  if elem != -1])
                            called = n
                            return unmarked * called
                        seen_indices.add(idx)

print(part1(text))
print(part2(text))