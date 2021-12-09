from collections import defaultdict

infile = "inputs/day5.txt"

marked = defaultdict(int)
with open(infile) as f:
    for line in f:
        res = line.strip().split()
        start = tuple(map(lambda x: int(x), res[0].split(',')))
        end = tuple(map(lambda x: int(x), res[2].split(',')))
        if start[0] == end[0]:
            step = -1 if start[1] > end[1] else 1
            for i in range(start[1], end[1] + step, step):
                marked[(start[0], i)] += 1
        elif start[1] == end[1]:
            step = -1 if start[0] > end[0] else 1
            for i in range(start[0], end[0] + step, step):
                marked[(i, start[1])] += 1
        elif abs(start[1] - end[1]) / abs(start[0] - end[0]) == 1:
            stepc = -1 if start[0] > end[0] else 1
            stepr = -1 if start[1] > end[1] else 1
            for cr in zip(range(start[0], end[0] + stepc, stepc),
                            range(start[1], end[1] + stepr, stepr)):
                    marked[cr] += 1

print(sum(value > 1 for value in marked.values()))
