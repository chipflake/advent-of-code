infile = "inputs/day6.txt"

days = 256
fish = dict.fromkeys(range(9), 0)

with open(infile) as f:
    fish_init = list(map(lambda x: int(x), f.readline().strip().split(',')))

for age in fish.keys():
    fish[age] = sum(i == age for i in fish_init)

for d in range(days):
    fish_old = dict(fish)
    for age in fish.keys():
        if age == 8:
            fish[age] = fish_old[0]
        elif age == 6:
            fish[age] = fish_old[age+1]
            fish[age] += fish_old[0]
        else:
            fish[age] = fish_old[age+1]
print(sum(fish.values()))
