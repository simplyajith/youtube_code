"""

https://leetcode.com/problems/jump-game-iii/submissions/

"""

# Solution1 : TopDpwn

class Solution:
	def canReach(self, arr, start: int) -> bool:
		
		n = len(arr)
		v = {}
		
		def get(arr, i):
			
			if i > n - 1 or v.get(i) or i < 0:
				return False
			
			if arr[i] == 0:
				return True
			
			#use visited, to prevent loops/cycles
			v[i] = True
			
			return get(arr, i - arr[i]) or get(arr, i + arr[i])
		
		return get(arr, start)


#Solution 2: BFS

class Solution:
	def canReach(self, arr, start: int) -> bool:
		
		n = len(arr)
		
		#Create the zero list with all zero indexes in list
		zero = []

		for idx, i in enumerate(arr):
			if i == 0:
				zero.append(idx)
		
		#Add start to the queue as BFS
		
		queue = []
		visited = {}
		queue.append(start)
		
		while queue:
			curr = queue.pop(0)
			if curr in zero:
				return True
			
			if curr not in visited and curr >= 0 and curr <= n - 1:
				visited[curr] = True
				queue.append(curr + arr[curr])
				queue.append(curr - arr[curr])
		
		return False
