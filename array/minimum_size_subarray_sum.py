"""

https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

Algorithm: Sliding window

"""

start_window = 0
end_window = 0
x = [1,4,4]
count = 0
window_sum = 0
s = 4
l = []
while end_window < len(x):
	
	window_sum += x[end_window]
	
	while window_sum >= s:
		l.append(end_window-start_window+1)
		window_sum = window_sum-x[start_window]
		start_window +=1
	
	end_window +=1
		
print(min(l))

