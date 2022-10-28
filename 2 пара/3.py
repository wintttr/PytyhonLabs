# найти колво локальных максимумов

def make_list():
    return list(map(int, input().split()))

lst = make_list()
cnt = 0
i = 1

while i + 1 < len(lst):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        cnt += 1
    i += 1

print(cnt)