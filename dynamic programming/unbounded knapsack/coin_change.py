"""
https://www.hackerrank.com/challenges/coin-change/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

"""

from sys import setrecursionlimit
limit = 1000000
setrecursionlimit(limit)
a = [1,2,3,8]
a =[2,5,3,6]
a =[1,2,3]
s =5
count = 0
def co(arr,n,sum1):
	global count
	print(arr,n,sum1)
	
	if sum1 == 0:
		count+=1
		return 1
	
	if sum1 <0:
		return 0
	if n ==-1:
		return 0
	
	if arr[n] <= sum1:
		return co(arr,n,sum1-arr[n])+co(arr,n-1,sum1)
	else:
		return co(arr,n-1,sum1)
		
n = len(a)
print(co(a,n-1,s))
print(count)



def co_m(arr, n, sum1,dp):
	global count
	print(arr, n, sum1,dp)
	
	if sum1 == 0:
		count += 1
		return 1
	
	if sum1 < 0:
		return 0
	if n == -1:
		return 0
	
	if dp[n][sum1] != "x":
		return dp[n][sum1]
	
	if arr[n] <= sum1:
		dp[n][sum1] = co_m(arr, n, sum1 - arr[n],dp)+co_m(arr, n - 1, sum1,dp)
		return dp[n][sum1]
	else:
		dp[n][sum1] = co_m(arr, n - 1, sum1,dp)
		return dp[n][sum1]


n = len(a)
dp = [["x" for _ in range(s+1)] for _ in range(len(a)+1) ]
print(co_m(a,n-1,s,dp))
# print(count)