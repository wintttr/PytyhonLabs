def get_pair():
	return tuple(map(str.capitalize, input().split()))

n = int(input())

d = dict()

for i in range(n):
	t1,t2 = get_pair()
	d[t1] = t2

print("Список пар, отсортированный по столицам:", sorted(d.items(), key = lambda u: u[1]))
print("Список пар, отсортированный по государствам:", sorted(d.items(), key = lambda u: u[0]))