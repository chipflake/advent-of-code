from statistics import median

opening = [ '(', '[', '{', '<' ]
closing = [ ')', ']', '}', '>' ]

match = dict(list(zip(opening, closing)) + list(zip(closing,opening)))

score =   { ')': 3, ']': 57, '}': 1197, '>': 25137 }
score_2 = { '(': 1, '[': 2,  '{': 3,    '<': 4 }

infile = "inputs/day10.txt"

with open(infile) as f:
    lines = list(map(str.strip, f.readlines()))

score_total = 0
all_scores_2 = []
for l in lines:
    s = []
    corrupted = False
    for c in l:
        if c in opening:
            s.append(c)
        elif s[-1] == match[c]:
            s.pop()
        else:
            # part 1
            score_total += score[c]
            corrupted = True
            break;
    # part 2
    if not corrupted and s:
        scoretmp = 0
        for c in reversed(s):
            scoretmp *= 5
            scoretmp += score_2[c]
        all_scores_2.append(scoretmp)

print(score_total)
print(median(all_scores_2))
