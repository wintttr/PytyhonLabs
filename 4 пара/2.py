def get_students():
	return set(map(str.capitalize, input().split()))

n = int(input("Введите количество учеников:"))

first = True

temp = get_students()
everyone = set(temp)
at_least_one = set(temp)

for i in range(n-1):
	st = get_students()
	everyone &= st
	at_least_one |= st

print("{} знает хотя бы один ученик: {}".format(len(at_least_one), at_least_one))

if(len(everyone) > 0):
	print("{} знают все: {}".format(len(everyone), everyone))
else:
	print("Нет языка, который знали бы все")