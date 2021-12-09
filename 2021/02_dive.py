infile = "inputs/day2.txt"

def part1(moves):
    hor, depth = 0, 0
    for move in moves:
        if move[0] == "forward":
            hor += move[1]
        elif move[0] == "up":
            depth -= move[1]
        elif move[0] == "down":
            depth += move[1]
        else:
            print("Invalid move")
    return hor*depth

def part2(moves):
    hor, depth, aim = 0, 0, 0
    for move in moves:
        if move[0] == "forward":
            hor += move[1]
            depth += (aim * move[1]) 
        elif move[0] == "up":
            aim -= move[1]
        elif move[0] == "down":
            aim += move[1]
        else:
            print("Invalid move")
    return hor*depth       

with open(infile) as f:
    moves = list(map(lambda x: ( x.split()[0], int(x.split()[1]) ), f.readlines()))

print(part1(moves))
print(part2(moves))
