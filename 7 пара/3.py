d = dict()
with open("input3.txt") as f:
    for i in f.read().split():
        d.setdefault(i, 0)
        d[i] += 1

nd = dict()
with open("output3.txt", mode="w") as f:
    for i in sorted(d.items(), key = lambda x: x[0]):
        nd.setdefault(i[1], [])
        nd[i[1]].append(i[0])

    for i in sorted(nd.items(), key = lambda x: x[0], reverse = True):
        f.write(" ".join(i[1]))

