infile = "inputs/day8.txt"

def contains(small, big):
    for c in small:
        if not c in big:
            return False
    return True

count = 0
summ  = 0
with open(infile) as f:
    for l in f:
        numbers, display = tuple(map(lambda x: x.split(" "), l.strip().split(" | ")))
        # part 1
        for d in display:
            if len(d) in [ 2, 3, 4, 7 ]:
                count += 1
        # part 2
        size_5, size_6 = [], []
        rep = dict.fromkeys(range(10), '')
        for n in numbers:
            if len(n) == 2:
                rep[1] = n
            elif len(n) == 3:
                rep[7] = n
            elif len(n) == 4:
                rep[4] = n
            elif len(n) == 5:
                size_5.append(n) # 2, 3, 5
            elif len(n) == 6:
                size_6.append(n) # 0, 6, 9
            elif len(n) == 7:
                rep[8] = n

        rep[3] = [ n for n in size_5 if contains(rep[1],n) ][0]
        size_5.remove(rep[3])
        rep[9] = [ n for n in size_6 if contains(rep[4],n) ][0]
        size_6.remove(rep[9])
        rep[0] = [ n for n in size_6 if contains(rep[1],n) ][0]
        size_6.remove(rep[0])
        rep[6] = size_6[0]
        rep[5] = [ n for n in size_5 if contains(n,rep[6]) ][0]
        size_5.remove(rep[5])
        rep[2] = size_5[0]

        inverted = { ''.join(sorted(k)) : v for v, k in rep.items() }
        mult = 1000
        for d in display:
            summ += inverted[''.join(sorted(d))] * mult
            mult //= 10
    print(count) # part 1
    print(summ)  # part 2
