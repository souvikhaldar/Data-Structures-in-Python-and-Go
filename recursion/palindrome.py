# Write a recursive function to check if a string is palindrome or not.  
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:len(s)-1])
    
s = input('Enter string: ')
val = palindrome(s)
print(val)