"""
Basecase:
if left>right:
    return True
else:
    if s[left] == s[right]:
        palindrome(s,left+1,right-1)
    else:
        return False

"""

def palindrome(s,left,right):
    if left > right:
        return True
    else:
        if s[left] == s[right]:
            return palindrome(s, left + 1, right - 1)
        else:
            return False

s ="malayalam"
print(palindrome(s,0,len(s)-1))
