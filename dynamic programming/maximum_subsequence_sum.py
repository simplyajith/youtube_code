from math import inf

def max_seq(arr,n, tot):
	# print(tot)
	if n == 1:
		return tot + arr[0]
	
	return max(max_seq(arr,n-1,tot+arr[n-1]), max_seq(arr,n-1,tot))

"""
Reference for dp :Zhe hus answer
#https://stackoverflow.com/questions/8649845/how-can-i-find-the-maximum-sum-of-a-sub-sequence-using-dynamic-programming/8649869#8649869
"""


def maxsequence(arr):

	memo = ["x" for _ in range(n)]
	memo[0] = max(0, arr[0])
	
	for i in range(1, n):
		memo[i] = max(memo[i - 1] + arr[i], memo[i - 1])
	
	localmax = memo[-1]
	
	#local max will be 0 only if all the numbers in array are negative
	#
	if localmax == 0:
		localmax = max(arr)
	
	return localmax


def maxSubarray(arr):
	localmax = -inf
	windowsum = 0
	endwindow = 0
	while endwindow < len(arr):
		windowsum += arr[endwindow]
		
		if arr[endwindow] > windowsum:
			windowsum = arr[endwindow]
		localmax = max(localmax, windowsum)
		endwindow += 1
	
	return localmax, maxsequence(arr)



# arr = [1,2,3,4]
arr = [-1,2,3,-4,5,10]
# arr =[2,-1,2,3,4,-5]
# arr = [-998,-9988]
n = len(arr)
print(max_seq(arr,n,max(0,arr[0])))

