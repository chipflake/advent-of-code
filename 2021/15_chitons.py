from queue import PriorityQueue

infile = "inputs/day15.txt"

M = 1   # change to 5 for Part 2
dirx = [-1, 0,  0, 1]
diry = [ 0, 1, -1, 0]

def is_valid(p):
    return not ( p[0] < 0 
        or p[0] >= M * size_x 
        or p[1] < 0 
        or p[1] >= M * size_y )

def get_neighbors(x, y):
    adj = zip([x + i for i in dirx], [y + j for j in diry])
    return [ n for n in adj if is_valid(n) ]

def risk_p1(x, y):
    return area[x][y]

def risk_p2(x, y):
    times_x = x // size_x
    times_y = y // size_y
    risk = area[x - times_x * size_x][y - times_y * size_y]
    for i in range(times_x + times_y):
        risk += 1
        if risk == 10:
            risk = 1
    return risk

# Choose risk function for part 1/2
get_risk = risk_p1

area = []
with open(infile) as f:
    for l in f:
        area.append(list(map(int, list(l.strip()))))
size_y = len(area[0])
size_x = len(area)

cost = [ [float('inf')] * M*size_y for i in range(M*size_x) ]
cost[0][0] = 0
visited = set()

pq = PriorityQueue()
pq.put((0, (0,0)))
while not pq.empty():
    (d, (x, y)) = pq.get(False)
    visited.add((x,y))
    for nx, ny in get_neighbors(x, y):
        distance = get_risk(nx, ny)
        if (nx, ny) not in visited:
            new_cost = cost[x][y] + distance 
            if new_cost < cost[nx][ny]:
                pq.put((new_cost, (nx, ny)))
                cost[nx][ny] = new_cost

print(cost[M*size_x-1][M*size_y-1])
