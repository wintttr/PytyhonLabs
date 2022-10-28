def equal5(l):
    if l[0] == l[1] == l[2] == l[3] == l[4]:
        return True
    else:
        return False

def equal4(l):
    temp = {}
    for i in l:
        temp.setdefault(i, 0)
        temp[i] += 1
    temp = sorted(temp.values())
    return len(temp) == 2 and temp[1] == 4

def equal32(l):
    temp = {}
    for i in l:
        temp.setdefault(i, 0)
        temp[i] += 1
    temp = sorted(temp.values())
    return len(temp) == 2 and temp[0] == 2 and temp[1] == 3

def monotone(l):
    l = sorted(l)
    return l[0] < l[1] < l[2] < l[3] < l[4]

def equal3(l):
    temp = {}
    for i in l:
        temp.setdefault(i, 0)
        temp[i] += 1
    temp = sorted(temp.values())
    return len(temp) == 3 and temp[2] == 3

def equal22(l):
    temp = {}
    for i in l:
        temp.setdefault(i, 0)
        temp[i] += 1
    temp = sorted(temp.values())
    return len(temp) == 3 and temp[1] == 2 and temp[2] == 2

def equal2(l):
    temp = {}
    for i in l:
        temp.setdefault(i, 0)
        temp[i] += 1
    temp = sorted(temp.values())
    return len(temp) == 4 and temp[3] == 2


s = input().split()

if len(s) != 5:
    exit()

if equal5(s):
    print("Impossible")
elif equal4(s):
    print("Four of a Kind")
elif equal32(s):
    print("Full House")
elif monotone(s):
    print("Straight")
elif equal3(s):
    print("Three of a Kind")
elif equal22(s):
    print("Two Pairs")
elif equal2(s):
    print("One Pair")
else:
    print("Nothing")
