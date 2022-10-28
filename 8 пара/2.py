def isPalindrom(x):
    return x == x[::-1]

def deleteAllNonAlphs(x):
    s = str()
    for c in x:
        if c.isalpha():
            print(c, "is alph")
            s += c
    return s

s = input()

print(isPalindrom(deleteAllNonAlphs(s.lower())))