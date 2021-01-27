v1 = input()
v2 = input()
v3 = input()
v4 = input()
v5 = input()
v6 = input()

w = 0
l = 0

if (v1 == "W"):
	w = w + 1
else:
	l = l + 1


if (v2 == "W"):
	w = w + 1
else:
	l = l + 1


if (v3 == "W"):
	w = w + 1
else:
	l = l + 1


if (v4 == "W"):
	w = w + 1
else:
	l = l + 1


if (v5 == "W"):
	w = w + 1
else:
	l = l + 1


if (v6 == "W"):
	w = w + 1
else:
	l = l + 1


if (w == 5 or w == 6):
	print(1)
elif (w == 3 or w == 4):
	print(2)
elif (w == 1 or w == 2):
	print(3)
else:
	print(-1)

