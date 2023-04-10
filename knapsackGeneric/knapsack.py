
def knapsack(maxWeight, itemWeights, itemValues, numOfItems):

	rowsMatrix = numOfItems+1 # First row is 0
	colsMatrix = maxWeight+1

	table = [[0 for _ in range(colsMatrix)] for _ in range(rowsMatrix)]

	for row in range(1, rowsMatrix): # Skipping first row
		for col in range(1, colsMatrix):
			ItemWeight = itemWeights[row-1]
			ItemValue = itemValues[row-1]
			
			previousValue = table[row-1][col]
			remainingSpace = col - ItemWeight
			valueOfRemainingSpace = table[row-1][remainingSpace]

			if ItemWeight <= col:
				table[row][col] = max(previousValue, ItemValue + valueOfRemainingSpace)
			else:
				table[row][col] = previousValue

	selectedItemsIndex = []
	# Starting from last index
	row = numOfItems 
	col = maxWeight

	while row > 0 and col > 0:
		currentCell = table[row][col]
		upperCell = table[row-1][col]
		if currentCell != upperCell:
			selectedItemsIndex.append(row-1)
			
			selectedItemWeight = itemWeights[row-1]
			col -= selectedItemWeight
		row -= 1

	optimalValue = table[numOfItems][maxWeight]

	return optimalValue,selectedItemsIndex

maxWeight = 4
itemWeights = [4, 3, 1]
itemValues = [3000, 2000, 1500]
numOfItems = len(itemWeights)
itemList = ["stereo","laptop","guitar"]

value, itemIndex = knapsack(maxWeight, itemWeights, itemValues, numOfItems)
items = [itemList[i] for i in itemIndex]
print(value, items)
