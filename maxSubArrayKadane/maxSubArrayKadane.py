def maxSubArray(nums):
	currSum = nums[0]
	maxSum = nums[0]

	for i in range(1,len(nums)):
		currSum = max(nums[i],nums[i] + currSum)
		maxSum = max(maxSum,currSum)

	return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
