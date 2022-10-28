def get_str():
	return list(map(str.lower, input().split()))

s = get_str()
d = dict()

for word in s:
	if word in d:
		d[word] += 1
	else:
		d[word] = 0

m = max(d.values())

lst = []
for t1, t2 in d.items():
	if(t2 == m):
		lst.append(t1)	

print(min(lst))

