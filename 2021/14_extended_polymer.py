from itertools import product
from string import ascii_uppercase

infile = "inputs/day14.txt"

steps = 40

rule = dict()
count = dict.fromkeys(product(ascii_uppercase, repeat=2), 0)
char_freq = dict.fromkeys(ascii_uppercase, 0)

with open(infile) as f:
    template = f.readline().strip()
    for l in f:
        if '->' in l:
            pair, letter = l.strip().split(' -> ')
            rule[tuple(pair)] = letter

last_char = template[-1]
for i in range(len(template)-1):
    count[template[i], template[i+1]] += 1

for s in range(steps):
    cur = [ (k, v) for k, v in count.items() if v > 0 ]
    for k, v in cur:
        s, e = k
        if (s, e) in rule:
            count[s, rule[s, e]] += v
            count[rule[s, e], e] += v
            count[s, e] -= v

char_freq[last_char] = 1
for s, e in [ k for k, v in count.items() if v > 0 ]:
    char_freq[s] += count[s, e]

print(max(char_freq.values()) - min([ v for v in char_freq.values() if v ]))
