"""

x = 	1	-3	2	1	-1
	
	
	Index	x[index]	window sum	Changed windowsum	max (localmax, changedwindowsum)	localmax
	0	1	1	1	1	1
	1	-3	-2	-2	1	1
	2	2	0	2	2	2
	3	1	1	3	3	3
	4	-1	0	3	3	3
	
"""

import math


class Solution:
	def maxSubArray(self, x) -> int:
		# Understanding, Kadanes algorithm
		
		# -2+1, -1
		localmax = -(math.inf)
		windowsum = 0
		end_window = 0
		
		while end_window < len(x):
			
			windowsum += x[end_window]

			if x[end_window] > windowsum:
				windowsum = x[end_window]
			localmax = max(localmax, windowsum)
	
			end_window += 1
		return localmax
	

#O(n**2) solution

def maxsubarray_brute_force(arr):
	maxi = -(math.inf)
	for i in range(len(arr)):
		tot = arr[i]
		maxi = max(maxi,tot)
		for j in range(i+1,len(arr)):
			tot +=arr[j]
			maxi = max(maxi, tot)
	return maxi
	
	
nums = [2,3,1,2,4,3]
# nums = [1,3,2,1,-1]
# nums = [-1,2,3,-4,5,10]
# nums = [2,-1,2,3,4,-5]
print(maxsubarray_brute_force(nums))
print(Solution().maxSubArray(nums))
	
