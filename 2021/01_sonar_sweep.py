infile = "inputs/day1.txt"

f = open(infile)
arr = list(map(int, f.readlines()))

# part 1
print(sum(map(lambda i:arr[i-1] < arr[i], range(1, len(arr)))))

# part 2
print(sum(map(lambda i:arr[i-3] < arr[i], range(3, len(arr)))))
