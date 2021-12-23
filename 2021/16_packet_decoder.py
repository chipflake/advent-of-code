from functools import reduce

infile = "inputs/day16.txt"

funs = {
        '000': sum,
        '001': lambda x: reduce(lambda a, b: a*b, x),
        '010': min,
        '011': max,
        '101': lambda x: int(x[0] > x[1]),
        '110': lambda x: int(x[0] < x[1]),
        '111': lambda x: int(x[0] == x[1]),
}

with open(infile) as f:
    arr = f.readline().strip()

msg = []
for i in list(arr):
    msg += bin(int(i, 16))[2:].zfill(4)
msg = ''.join(msg)
versions = []

def parse_packet(s):
    versions.append(msg[s:s+3])
    tid = msg[s+3:s+6]
    if tid == '100':
        n, val = parse_literal(s+6)
        return n, val
    else:
        return parse_operator(s+6, tid)

def parse_literal(s):
    i = s
    val = ''
    while msg[i] != '0':
        val += msg[i+1:i+5]
        i += 5    
    val += msg[i+1:i+5]
    i += 5
    return i, int(val,2)

def parse_operator(s, op):
    vals = []
    if msg[s] == '0':
        sub_len = int(msg[s+1:s+16], 2)
        ns = s + 16
        while ns < s + 16 + sub_len:
            ns, val = parse_packet(ns)
            vals.append(val)
    else:
        sub_num = int(msg[s+1:s+12], 2)
        ns = s + 12
        for i in range(sub_num):
            ns, val = parse_packet(ns)
            vals.append(val)
    return ns, funs[op](vals)

# part 2
print(parse_packet(0)[1])
# part 1
print(sum([ int(v,2) for v in versions ] ))
