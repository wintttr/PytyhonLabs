with open("input2.txt") as f:
    for line in f:
        s = sum(list(map(int, line.split())))
        print(s)