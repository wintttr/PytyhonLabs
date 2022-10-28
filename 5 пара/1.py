def get_pair():
	return tuple(map(str.lower, input().split()))

n = int(input("Введите число пар синонимов: "))

print("Введите все пары слов:")

d_syn = dict()
for _ in range(n):
	t1, t2 = get_pair()
	d_syn[t1] = t2
	d_syn[t2] = t1

word = input("Введите слово, для которого нужно найти синоним: ").lower()

if not word in d_syn:
	print("Синонима для слова \"{}\" нет".format(word.capitalize()))
else:
	print("Синоним для слова \"{}\" - \"{}\"".format(word.capitalize(), d_syn[word].capitalize()))