infile = "inputs/day3.txt"

def part_one(numbers, size):
    ones = [0] * size
    for i in range(size):
        ones[i] = sum(int(num[i]) for num in numbers) 
    g, e = 0, 0
    total = len(numbers)
    for i, v in enumerate(reversed(ones)):
        if 2 * v > total:
            g += 2**i
        else:
            e += 2**i
    return g*e

def part_two(numbers, size, compare):
    res = numbers[:]
    for i in range(size):
        ones = sum(int(num[i]) for num in res)
        if compare(2 * ones, len(res)):
            digit = '1'
        else:
            digit = '0'
        res = [ num for num in res if num[i] == digit ]
        if len(res) == 1:
            return res[0]

with open(infile) as f:
    numbers = list(map(lambda x: x.strip(), f.readlines()))

print(part_one(numbers, len(numbers[0])))

oxygen = part_two(numbers, len(numbers[0]), lambda x,y: x >= y)
co2 = part_two(numbers, len(numbers[0]), lambda x,y: x < y)
print(int(oxygen, 2)*int(co2, 2))
