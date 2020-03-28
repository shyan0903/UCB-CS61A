def merge(s1,s2):
	if s1 == [] or s2 == []:
		return s1 + s2
	elif s1[0] <= s2[0]:
		return [s1[0]] + merge(s1[1:], s2)
	else:
		return [s2[0]] + merge(s1, s2[1:])
