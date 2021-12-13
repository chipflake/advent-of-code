from collections import defaultdict

infile = "inputs/day12.txt"

def dfs(cur):
    if cur == "end":
        return 1
    visited[cur] += 1
    path_count = 0
    for n in graph[cur]:
        # part 1
        if n.islower() and visited[n] > 0:
            # part 2
            if len([ (k, v) for k, v in visited.items() if k.islower() and v > 1]) > 0:
                continue
        path_count += dfs(n)
    visited[cur] -= 1
    return path_count

graph = defaultdict(set)
with open(infile) as f:
    for l in f:
        s, e = l.strip().split('-')
        graph[s].add(e)
        if not s == 'start':
            graph[e].add(s)

visited = dict.fromkeys(graph.keys(), 0)
print(dfs('start'))
