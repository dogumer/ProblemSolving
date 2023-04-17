def partition(array,start,end):
	pivot = array[end]
	i = start-1

	for j in range(start,end):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]

	array[i+1], array[end] = array[end], array[i+1]

	return i + 1

def quickSort(array,start,end):
	if start < end: # base case
		
		pivot = partition(array,start,end)
		quickSort(array,start,pivot-1)
		quickSort(array,pivot+1,end)

		return array

print(quickSort([4,6,7,0,9,1,2,5,3,8],0,9)) 
