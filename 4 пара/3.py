lst = []
k = int(input())
n = int(input())

for i in range(n):
    s = list(map(int, input().split()))
    lst.append((s[0], s[1]))

count = 0

for i in range(k):
    if i % 7 >= 5:
        continue
    else:
        flag = True
        for (x, y) in lst:
            if (i - x) % y != 0:
                continue
            else:
                flag = False
                break
        if flag:
            count += 1
print(count)
