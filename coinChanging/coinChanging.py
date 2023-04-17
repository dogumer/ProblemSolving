def coinChanging(coins,total):
	table = [[0 for _ in range(total+1)] for _ in range(len(coins)+1)]
	table[0] = [x for x in range(total+1)]
	
	for i in range(1,len(coins)+1):
		for j in range(1,total+1):
			if j >= coins[i-1]:
				table[i][j] = min(table[i-1][j],1+table[i][j-coins[i-1]])
			else:
				table[i][j] = table[i-1][j]

	return table[len(coins)][total]

print(coinChanging([1,5,6],11))
