s = input()

s = s.split()
s = " ".join(s)
s = s.replace(" ,", ",")
s = s.replace(" .", ".")
s = s.replace(", ", ",")
s = s.replace(". ", ".")
s = s.replace(",", ", ")
s = s.replace(".", ". ")

print(s)