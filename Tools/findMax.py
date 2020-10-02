findMaxA(l):

	l.sort()
	return l[len(l) -1]

findMaxB(l):

	m = l[0]

	for i in range(0, len(l), 1):
		if l[i] > m:
			m = l[i]

	return m


l = [100,1,3,5,3,1234,423,5432,5423]
print (max(l))