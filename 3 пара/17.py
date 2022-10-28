#  17

# d2 и d3 точно лежат на OX
def area_impl(d1, d2, d3):
	return abs((d2[0] - d3[0])*d1[1])/2

# какие-нибудь 2 точки лежат на OX
def area(d1, d2, d3):
	if(d1[1] == 0 and d2[1] == 0):
		return area_impl(d3, d1, d2)
	if(d2[1] == 0 and d3[1] == 0):
		return area_impl(d1, d2, d3)
	if(d1[1] == 0 and d3[1] == 0):
		return area_impl(d2, d1, d3)

def check(d1, d2, d3):
	if(d1[1] == 0 and d2[1] == 0 or d1[1] == 0 and d3[1] == 0 or d2[1] == 0 and d3[1] == 0):
		return True
	else:
		return False

def input_pair():
	return tuple(map(int, input().split()))

lst = []

m = 0
n = int(input())
 	
for _ in range(n):
	dot = input_pair()
	if(len(lst) < 3):
		lst.append(dot)
	else:
		if(check(lst[0], lst[1], lst[2])):
			m = max(area(lst[0], lst[1], lst[2]), m)
		if(check(lst[0], lst[1], dot)):
			m = max(area(lst[0], lst[1], dot), m)
			lst[2] = dot
		if(check(lst[0], dot, lst[2])):
			m = max(area(lst[0], dot, lst[2]), m)
			lst[1] = dot
		if(check(dot, lst[1], lst[2])):
			m = max(area(dot, lst[1], lst[2]), m)
			lst[0] = dot

print(int(m) if int(m) == m else m)