def longestCommonSubsequence(str1,str2):
	len1, len2 = len(str1), len(str2)

	# Create table full of zeros
	table = [[0] * (len2+1) for _ in range(len1+1)] # 0th line and column are 0

	# Fill table using algorithm
	for i in range(1,len1+1): # Skipping first index
		for j in range(1, len2+1):
			if str1[i-1] == str2[j-1]:
				crossCell = table[i-1][j-1]
				table[i][j] = crossCell + 1
			else:
				leftCell, upperCell = table[i][j-1] ,table[i-1][j]
				table[i][j] = max(leftCell, upperCell)

	# Backtrack for lcs
	i, j = len1, len2
	lcs = ""
	while i > 0 and j > 0:
		leftCell, upperCell = table[i][j-1] ,table[i-1][j]

		if str1[i-1] == str2[j-1]:
			lcs = str1[i-1] + lcs
			i -= 1
			j -= 1
		elif upperCell > leftCell:
			i -= 1
		else:
			j -= 1

	return lcs

print(longestCommonSubsequence("dogukan","batuhan"))
