"""
https://leetcode.com/problems/jump-game/
"""
#74/75 passed
#Solution 1
from sys import setrecursionlimit

limit = 1000000
setrecursionlimit(limit)


class Solution:
	
	def canJump(self, nums) -> bool:

		
		def j(arr, i, memo):

			if i >= len(arr) - 1:
				return True
			
			if i in memo:
				return memo[i]
			
			if arr[i] > 0:
				for v in range(arr[i], 0, -1):
					memo[i + v] = j(arr, i + v, memo)
		
		memo = {}
		j(nums, 0, memo)
		if True in memo.values():
			return True


"""
Failed Test case: https://leetcode.com/submissions/detail/352725509/testcase/
"""

#74/75 passed
class Solution:
	
	def canJump(self, nums) -> bool:
		

		memo = [False for _ in range(len(nums))]
		
		memo[-1] = True
		
		for i in range(len(nums) - 2, -1, -1):
			for j in range(nums[i], -1, -1):
				
				if j + i >= len(nums) -1 or memo[j + i]:
					memo[i] = memo[-1]
					break
		
		return memo[0]


#75/75 passed
class Solution:
	
	def canJump(self, nums) -> bool:
		
		n = len(nums)
		last_good_pos = n-1
		
		for i in range(len(nums)-1,-1,-1):
			
			if i+nums[i] >=last_good_pos:
				last_good_pos = i
				
		if last_good_pos == 0:
			return True
		
		return False
		