alphs = 0
nalphs = set()
words = 0

with open("input5.txt") as f:
    s = f.read()
    for i in s:
        if str.isalpha(i):
            alphs += 1
        else:
            nalphs.add(i)
    for i in nalphs:
        s.replace(i, " ")
    for i in s.split():
        if str.isalpha(i):
            words += 1


print(alphs)
print(words)