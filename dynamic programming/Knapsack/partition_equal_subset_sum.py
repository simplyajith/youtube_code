"""


416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
"""
Algorithm:

Need to partition the subsets into two with same sum, it implies that both the subset has to be sum // 2.

Hence find subsets with sum equal to sum//2.

1. choice:
      An index in the given array is part of subset or its not a part of subset.
    
2. Base condition:
     minimal Valid condition : when array length is 0, sum =0.
     
Start from the last index of the array and recurse with the choices.


"""
count = 0
# arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
arr = [1,5,11,5,4,2]
# arr = [1,2,3,5,1]
x = sum(arr)

memo = [["x" for _ in range((sum(arr))+1)]for _ in range(len(arr)+1)]

sum1 = sum(arr) // 2
# print(sum1)

def subsetsum(arr, n, halfsum, calc_sum):
	global count
	print(arr,n,halfsum,calc_sum)
	
	if memo[n][calc_sum] != "x":
		return memo[n][calc_sum]
	
	if halfsum == calc_sum:
		print(calc_sum)
		count+=1
		# return count
	
	if n == 0:
		return 0
	
	memo[n][calc_sum] = subsetsum(arr,n-1,halfsum,calc_sum+arr[n-1])
	memo[n][calc_sum] = subsetsum(arr,n-1,halfsum,calc_sum)

subsetsum(arr,len(arr),sum1,0)
print(memo)
print(count)
