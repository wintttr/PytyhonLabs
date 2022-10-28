s = input().split()

d = dict()
for word in s:
	if word in d:
		print("{} встречалось {} раз".format(word, d[word]))
		d[word] += 1
	else:
		print("{} встречалось 0 раз".format(word))
		d[word] = 1