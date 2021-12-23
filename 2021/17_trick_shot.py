import re

puzz_in = "target area: x=153..199, y=-114..-75"

lim_x, lim_y = re.findall(r'([+-]?\d+)..([+-]?\d+)', puzz_in)
lim_x = tuple(map(int, lim_x))
lim_y = tuple(map(int, lim_y))

def hit(x, y):
    return (lim_x[0] <= x <= lim_x[1]) and (lim_y[0] <= y <= lim_y[1])

def shoot(vx, vy):
    px, py = 0, 0
    maxy = 0
    while px <= lim_x[1] and py >= lim_y[0]:
        px += vx
        py += vy
        maxy = max(maxy, py)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if hit(px, py):
            return maxy
    return None

total_max = 0   # part 1
count = 0       # part 2
# ╮(╯ _╰ )╭
for x in range(-200, lim_x[1] + 1):
    for y in range(-1000, 1000):
        res = shoot(x,y)
        if res is not None:
            count += 1
            total_max = max(total_max, res)
print(total_max, count)
