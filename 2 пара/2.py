# макс длину монотонного фрагмента

def make_list():
    return list(map(int, input().split()))

lst = make_list()

m = 0
dir = True # True >, False <

i = 0
while(i + 1 < len(lst)):
    cnt = 1
    if lst[i] > lst[i+1]:
        dir = True
    else:
        dir = False

    while(i + 1 < len(lst)):
        if(lst[i] > lst[i+1] and dir == True):
            cnt +=1
            i += 1
        elif(lst[i] < lst[i+1] and dir == False):
            cnt += 1
            i += 1
        else:
            break
    m = max(m, cnt)

print(m)