"""

https://www.hackerrank.com/challenges/unbounded-knapsack/problem
"""

from sys import setrecursionlimit
limit = 1000000
setrecursionlimit(limit)


"""
Solution 1:
Find the max

"""


def unboundedKnapsack(k, arr):
	def knap(val, sum1, memo):
		# print(val,sum1)
		# print(memo)
		
		if sum1 > k:
			return 0
		
		if val < 0:
			return 0
		
		if memo[val][sum1] != "x":
			return memo[val][sum1]
		
		if arr[val] <= k:
			memo[val][sum1] = max(knap(val, sum1 + arr[val], memo), knap(val - 1, sum1, memo))
			res.append(sum1)
			return memo[val][sum1]
		else:
			memo[val][sum1] = knap(val - 1, sum1, memo)
			res.append(sum1)
			# print(sum1)
			return memo[val][sum1]
	
	res = []
	n = len(arr)
	# print(n)
	memo = [["x" for _ in range(k + 1)] for _ in range(n + 1)]
	# print(memo)
	knap(n - 1, 0, memo)
	return (max(res))





"""
Solution 2:
Find the min and return the difference

"""
def unbounded_knapsack_r(arr,n, sum1,a_sum):
	# print(arr,n,sum1)
	if n==-1 and sum1 !=0:
		if sum1 > arr[n]:
			return sum1-arr[n]
		else:
			return sum1
	
	if n == -1:
		return 0

	
	if arr[n] <= sum1 and sum1 <= a_sum:
		return min(unbounded_knapsack_r(arr,n,sum1-arr[n],a_sum),unbounded_knapsack_r(arr,n-1, sum1,a_sum))
	else:
		return unbounded_knapsack_r(arr, n - 1, sum1,a_sum)
	
# arr = [3,7,9]
arr=[2,3,4]
n = len(arr)
# print(unbounded_knapsack_r(arr,n-1,11,11))


def unbounded_knapsack_memo(arr, n, sum1, memo):
	# print(arr,n,sum1)
	if memo[n][sum1] != "x":
		return memo[n][sum1]
	
	if n == -1 and sum1 != 0:
		if sum1 > arr[n]:
			return sum1 - arr[n]
		else:
			return sum1
	
	if n == -1:
		return 0
	
	if arr[n] <= sum1:
		memo[n][sum1] = min(unbounded_knapsack_memo(arr, n, sum1 - arr[n], memo), unbounded_knapsack_memo(arr, n - 1, sum1, memo))
		return memo[n][sum1]
	else:
		memo[n][sum1] = unbounded_knapsack_memo(arr, n - 1, sum1, memo)
		return memo[n][sum1]


def unboundedKnapsack(k, arr):
	n = len(arr)
	memo = [["x" for _ in range(k + 1)] for _ in range(n + 1)]
	return k - unbounded_knapsack_memo(arr, n - 1, k, memo)






# def unbounded_knapsack_dp(arr, sum1):
# 	l = len(arr)
# 	memo = [["x" for _ in range(sum1)] for _  in range(l)]
# 	# mini = math.inf
# 	for i in range(l):
# 		for j in range(sum1):
#
# 			if i == 0 and j!= 0:
# 				if j > arr[i]:
# 					memo[i][j] = j-arr[i]
#
# 				else:
# 					memo[i][j] = j
#
# 			elif i == 0:
# 				memo[i][j] = 0
#
# 			# not sure what to put when j is 0 , 0 or arr[i]
# 			elif j == 0:
# 				memo[i][j] = 0
#
#
# 			else:
#
# 				if arr[i] <= j:
# 					# print(i,j)
# 					memo[i][j] = min(memo[i][j-arr[i]],memo[i-1][j])
# 					if memo[i][j] == 0:
# 						print(memo[i][j],i ,j)
#
# 				else:
# 					memo[i][j] = memo[i-1][j]
# 					if memo[i][j] == 0:
# 						print(memo[i][j], i, j)


# arr=[2,3,4]
# arr=[3,7,9]
# n = len(arr)
# print(unbounded_knapsack1(arr,11))