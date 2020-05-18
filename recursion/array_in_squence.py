"""
Base case:
if idx == len(arr)-2:
    return arr[idx]+1 == arr[idx+1]
else:
    if arr[idx+1]-arr[idx]==1:
        return insequence(idx+1,arr)
"""

def array_in_sequence(idx,arr):

    if idx == len(arr) - 2:
        return arr[idx] + 1 == arr[idx + 1]
    else:
        if arr[idx + 1] - arr[idx] == 1:
            return array_in_sequence(idx + 1, arr)
        else:
            return False

arr =[1,2,4,4,6]
print(array_in_sequence(0,arr))