
"""
finding subsets with bfs
 
 List all the subsets of an array
 
https://leetcode.com/problems/subsets/
https://leetcode.com/problems/subsets-ii/

arr = [1,2,3]
subset = [[]]

Level 1:  When you add empty subset ([]) with [1], we get [1]
subset = [[], [1]]

Level 2:  now add [2] with members in subset, [] + [2] = [2] , [1] +[2] = [1,2]
subset = [[], [1],[2],[1,2]]

Level 3: now add [3] with members in subset, [] + [3] = [3],[1] +[3] = [1,3], [2] +[3] = [2,3], [1,2] + [3] =[1,2,3]
subset = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
"""


def bfs_subset(arr):
	sub = [[]]
	while arr:
		
		curr = arr.pop(0)
		
		for i in range(len(sub)):
			sub.append(sub[i] + [curr])
	
	return sub


arr1 = [1, 2, 3]
print(bfs_subset(arr1))

# s =[2]
#
# v =[1]
#
# print(s+v)
# v1 =[1,2]
#
# for i in v1:
# 	print(s + [i])








