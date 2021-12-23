infile = "inputs/day13.txt"

# TODO set
origami = dict()
folds = []
with open(infile) as f:
    for l in f:
        if ','in l:
            x, y = map(int,l.strip().split(','))
            origami[x, y] = '#'
        elif 'fold' in l:
            folds.append(tuple(l.strip().split(" ")[2].split("=")))

part1 = True
for dim, loc in folds:
    loc = int(loc)
    to_add = dict()
    to_remove = []
    if dim == 'y':
        for x, y in origami:
            if y > loc:
                to_add[(x, 2*loc - y)] = '#'
                to_remove.append((x, y))
    if dim == 'x':
        for x, y in origami:
            if x > loc:
                to_add[(2*loc - x, y)] = '#'
                to_remove.append((x, y))
    origami.update(to_add)
    for k in to_remove:
        origami.pop(k)
    if part1:
        print(len(origami))
        part1 = False

max_x, max_y = 0, 0
for x, y in origami.keys():
    max_y = max(y, max_y)
    max_x = max(x, max_x)

for y in range(max_y + 1):
    for x in range(max_x + 1):
        print('#' if (x, y) in origami else '.', end='')
    print()
