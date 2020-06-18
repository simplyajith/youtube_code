"""
Edit distance
A = []
https://www.coursera.org/learn/algorithmic-toolbox/lecture/TAveS/computing-edit-distance
Algorithm:

minimum insertions, minim deletion, minimum mismatch.

If insertions, adding 1 in A[i]for the same A[i]B[j-1] + 1
If deletions, deleting 1 letter in A[i-1]B[j]+1
mismatch, a[i-1]B[j-1]+1  if i!=j
match , A[i-i], B[j-1]    if i == j


Hence
 
 if a[i] != b[j]:
 	d(i,j) =min( d(i,j-1)+1, d(i-1,j)+1,(d-1,j-1)+1)
if a[i] == b[j]:
	d(i,j) =min( d(i,j-1)+1, d(i-1,j)+1,(d-1,j-1))

"""



def edit_distance(a : str,b : str):
	
	n = len(a)
	m = len(b)
	mem = [[0 for _ in range(m+1)] for _ in range(n+1)]
	
	#initialization
	for i in range(n+1):
		for j in range(m+1):
			if i ==0:
				mem[i][j] = j
			elif j == 0:
				mem[i][j]= i
	
	#updating the condition
	for i in range(1,n+1):
		for j in range(1,m+1):
			if a[i-1]!=b[j-1]:
				mem[i][j] = min(mem[i][j-1]+1, mem[i-1][j]+1, mem[i-1][j-1]+1)
			else:
				mem[i][j] = min(mem[i][j - 1] + 1, mem[i - 1][j] + 1, mem[i - 1][j - 1])
			
	
	print(mem)
	return mem[n][m]
	

	
# print(edit_distance("editing","distance"))
print(edit_distance("bread","really"))





