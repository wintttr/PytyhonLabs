# найти минимальное расстояние между локальными максимумами

def make_list():
    return list(map(int, input().split()))


lst = make_list()
local_max = []

for i in range(1, len(lst)-1)
    if lst[i-1] < lst[i] and lst[i] > lst[i + 1]:
        local_max.append(i)

i = 0
m = abs(local_max[0] - local_max[1]) if len(local_max) > 1 else 0
while(i + 1 < len(local_max)):
    m = min(m, abs(local_max[i] - local_max[i+1]))
    i += 1

print(m if m > 0 else "Локальных максимумов нет")