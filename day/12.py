from collections import defaultdict

f = open('test/12.txt', 'r')
text = f.read()

def dfs(graph, current, goal, all_paths, path):
    path = path + [current]
    if current == goal:
        all_paths.append(path)
    for node in graph[current]:
        if node not in path or (node in path and not node.islower()):
            dfs(graph, node, goal, all_paths, path)

def new_dfs(graph, current, goal, all_paths, path):
    path = path + [current]
    if current == goal:
        all_paths.append(path)
    for node in graph[current]:
        if node not in path or (node in path and not node.islower()) \
            or (node in path and node.islower() and node not in ["end", "start"] and path.count(node) <= 1 \
                and all(path.count(n) <= 1 for n in path if n.islower() and n != node)):
            new_dfs(graph, node, goal, all_paths, path)

def part1(text):
    lines = text.split("\n")
    paths = defaultdict(lambda: [])
    for l in lines:
        start, end = l.split("-")
        paths[start].append(end)
        paths[end].append(start)
    all_paths = []
    dfs(paths, "start", "end", all_paths, [])
    return len(all_paths)

def part2(text):
    lines = text.split("\n")
    paths = defaultdict(lambda: [])
    for l in lines:
        start, end = l.split("-")
        paths[start].append(end)
        paths[end].append(start)
    all_paths = []
    new_dfs(paths, "start", "end", all_paths, [])
    return len(all_paths)

print(part1(text))
print(part2(text))