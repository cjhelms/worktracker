def isPermutation(s1, s2):
	letterCount1 = {}
	letterCount2 = {}
	for i in range(0,len(s1)-1):
		if s1[i] in letterCount1:
			letterCount1[i] = letterCount1[i] + 1
		else:
			letterCount1[i] = 1
		if s2[i] in letterCount2:
			letterCount2[i] = letterCount2[i] + 1
		else:
			letterCount2[i] = 1
	for key in letterCount1:
		if key not in letterCount2:
			return False
		if letterCount1[key] != letterCount2[key]:
			return False
	return True
