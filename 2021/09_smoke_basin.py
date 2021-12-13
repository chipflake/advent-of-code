from bisect import insort
from collections import deque
from functools import reduce
# TODO namedtuple?

dirx = [-1, 0,  0, 1]
diry = [ 0, 1, -1, 0]

def is_valid(p):
    #TODO split per dimension
    return not ( p[0] < 0 or p[0] >= size_x or p[1] < 0 or p[1] >= size_y )

def get_neighbors(x, y):
    adj = zip([x + i for i in dirx], [y + j for j in diry])
    return [ n for n in adj if is_valid(n) ]

infile = "inputs/day9.txt"

area = []
with open(infile) as f:
    for l in f:
        area.append(list(map(int, list(l.strip()))))
size_y = len(area[0])
size_x = len(area)

# part 1
total = 0
low_points = []
for x in range(size_x):
    for y in range(size_y):
        if all([ area[nx][ny] > area[x][y] for nx, ny in get_neighbors(x, y) ]):
            total += area[x][y] + 1
            low_points.append((x,y))
print(total)

# part 2
visited = [ [False] * size_y for i in range(size_x) ]
sizes = []
for lpx, lpy in low_points:
    if visited[lpx][lpy]:
        continue
    q = deque()
    q.append((lpx, lpy))
    visited[lpx][lpy] = True
    cur_size = 0
    while q:
        x, y = q.popleft()
        if area[x][y] == 9:
            continue
        cur_size += 1
        neigh = zip([x + i for i in dirx], [y + j for j in diry])
        for nx, ny in neigh:
            if is_valid((nx, ny)) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    insort(sizes, cur_size)
print(reduce(lambda x, y: x*y, sizes[-3:]))
