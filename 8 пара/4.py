def isPalindrom(x):
    return x == x[::-1]

s = input()

max_pal = 1

for i in range(len(s)):
    if(isPalindrom(s[i::])):
        max_pal = i
        break

if max_pal < len(s) and max_pal > 0:
    s += s[max_pal::-1]

print(s)
