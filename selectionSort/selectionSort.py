def selectionSort(array,index):
	while index < len(array):
		array[array.index(min(array[index:]))], array[index] = array[index], array[array.index(min(array[index:]))]
		index += 1
	return array

print(selectionSort([2,1,6,7,0,9],0))