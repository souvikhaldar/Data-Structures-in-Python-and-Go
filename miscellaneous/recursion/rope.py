# Given a rope of length `n`, you need to find maximum number 
# of pieces you can make such that length of every piece is in 
# set {a,b,c} for given three values a,b and c. 
def rope(ropeLength,availSizes,i,maxi,count):
        print("ropeLength {}: availSizes {}: i {}: maxi {} : ".format(ropeLength,availSizes,i,maxi))
        if i == len(availSizes):
                return maxi
        if ropeLength % availSizes[i] == 0:
                count = count + ropeLength / availSizes[i]
                if maxi < count:
                        maxi = count
                return rope(ropeLength,availSizes,i+1,maxi,count)
        else:
                rem = ropeLength % availSizes[i] 
                count = count + ropeLength // availSizes[i]
                if maxi < count:
                        maxi = count
                return rope(rem,availSizes,i+1,maxi,count)

print(rope(5,[2,5,1],0,0,0))


