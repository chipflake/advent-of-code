infile = "inputs/day4.txt"

def mark(board, value):
    for row in board:
        for box in row:
            if value == box[0]:
                box[1] = True

def board_wins(board):
    for row in range(5):
        if all([ x for x in map(lambda a: a[1], board[row])]):
            return True
    for col in range(5):
        if all([ x for x in map(lambda a: a[1], 
                [ board[i][col] for i in range(5) ])]):
            return True

def get_score(board, num):
    total_sum = 0
    for row in board:
        for box in row:
            if not box[1]:
                total_sum += box[0]
    return (total_sum * num)

def bingo(numbers, boards):
    for num in numbers:
        for board in boards:
            mark(board, num)
            if board_wins(board):
                return (board, num)

def no_bingo(numbers, boards):
    for num in numbers:
        for board in list(boards):
            mark(board, num)
            if board_wins(board):
                boards.remove(board)
                if len(boards) == 0:
                    return (board, num)

with open(infile) as f:
    numbers = list(map(lambda x: int(x), 
                f.readline().strip().split(',')))
    next(f)
    boards, cur = [], []
    for line in f:
        if line == '\n':
            boards.append(cur)
            cur = []
        else:
            cur.append(list(map(lambda x: [int(x), False],
                line.strip().split())))
    boards.append(cur)

# part 1
win_board, num = bingo(numbers, boards)
print(get_score(win_board, num))

# part 2
last_win_board, num = no_bingo(numbers, boards)
print(get_score(last_win_board, num))
