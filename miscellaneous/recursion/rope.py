# Given a rope of length `n`, you need to find maximum number 
# of pieces you can make such that length of every piece is in 
# set {a,b,c} for given three values a,b and c. 
def rope(n,s,i,maxi):
    print("maxi: ",maxi)
    if i == len(s) - 1:
        return maxi
    rem = n % s[i]
    print("rem: ",rem)
    if rem == 0:
        maxi = max(maxi,n/s[i])
    else:
        return rope(rem,s,i+1,maxi)
print(rope(5,[2,5,1],0,0))