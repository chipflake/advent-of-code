from collections import deque
from itertools import product

dirx = [-1, 0,  0, 1, -1, -1,  1, 1]
diry = [ 0, 1, -1, 0, -1,  1, -1, 1]

def is_valid(p):
    return not ( p[0] < 0 or p[0] >= size_x or p[1] < 0 or p[1] >= size_y )

def neighbors(x, y):
    adj = zip([x + i for i in dirx], [y + j for j in diry])
    return [ n for n in adj if is_valid(n) ]

infile = "inputs/day11.txt"

area = []
with open(infile) as f:
    for l in f:
        area.append(list(map(int, list(l.strip()))))
size_y = len(area[0])
size_x = len(area)

step = 0
total_flashes, cur_flashes = 0, 0
while cur_flashes < size_y * size_x:
    cur_flashes = 0
    fl = deque()
    for x, y in product(range(size_x), range(size_y)):
        if area[x][y] == 9:
            fl.append((x, y))
        else:
            area[x][y] += 1
    while fl:
        px, py = fl.popleft()
        if area[px][py] == 0:
            continue
        area[px][py] = 0
        cur_flashes += 1
        for nx, ny in neighbors(px, py):
            if area[nx][ny] == 0:
                continue
            area[nx][ny] += 1
            if area[nx][ny] > 9:
                fl.append((nx, ny))
    step += 1
    total_flashes += cur_flashes
    # part 1
    if step == 100:
        print(total_flashes)
# part 2
print(step)
