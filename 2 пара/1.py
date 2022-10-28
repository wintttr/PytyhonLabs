# список найти макс количество идущих подряд равных элементов

def make_list():
    return list(map(int, input().split()))

lst = make_list()

cnt = 1
m = 0

i = 0
while(i < len(lst)):
    last = lst[i]
    cnt = 0
    while(i < len(lst)):
        if(lst[i] == last):
            cnt += 1
            i += 1
        else:
            break
    m = max(m, cnt)

print(m)