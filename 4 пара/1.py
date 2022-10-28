def get_colors():
	return set(map(str.capitalize, input().split()))

first = get_colors()
second = get_colors()

uni = first | second
intersect = first & second

print("{} хотя бы у одного: {}".format(len(uni), uni))
print("{} у обоих: {}".format(len(intersect), intersect))