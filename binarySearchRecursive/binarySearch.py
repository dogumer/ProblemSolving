def binarySearch(array,target,left,right):
	if right >= left:
		mid = left + (right-left) // 2

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			return binarySearch(array,target,left,mid-1)
		else:
			return binarySearch(array,target,mid+1,right)
	else:
		return -1

print(binarySearch([1,4,5,6,7,8,19,45],8,0,7)) 
