"""
Base case:
if index == end of list:
    return maximum

else:
    maximum = max(A[i],maximum,A[i+1])

"""

def maxi(idx,maximum,a):

    if idx == len(a)-1:
        return max(a[idx],maximum)
    else:
        maximum = max(a[idx],maximum)
        print(maximum)
        idx += 1
        return maxi(idx,maximum,a)

a = [100,2000,3,4,1,10,1001]
print(maxi(0,-1234,a))