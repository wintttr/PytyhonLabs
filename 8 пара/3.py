n = int(input())

x = "1 "
for _ in range(n-1):
    new_x = ""
    cnt = 0
    last = x[0]
    for j in x:
        if last == j:
            cnt += 1
        else:
            new_x += str(cnt) + last
            last = j
    x = new_x + " "

print(x)
