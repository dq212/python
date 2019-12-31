#test to see if the input is a palindrome

def reverse(s):
    return s[::-1] 

def isPalindrome(s):
    rev = reverse(s)

    if (s==rev):
        return True
    return False

s = "racecar1"
ans = isPalindrome(s)
print(isPalindrome(s))
