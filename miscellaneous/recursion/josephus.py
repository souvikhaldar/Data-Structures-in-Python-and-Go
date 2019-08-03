# Given `n` people in a circle, `kth` person is killed in every iteration. 
# Find the survivor. (Josephus Problem)

def josephus(n,k,start,i,killed=[]):
    
    if n == len(killed) + 1:
        return set([x for x in range(1,n+1)]) - set(killed)
    if (start+1)%n == 0:
        next = 7
    else:
        next = (start+1)%n
    if start in killed:
        return josephus(n,k,next,i,killed)
    else:
        if i == k:
            killed.append(start)
            return josephus(n,k,start,1,killed)
        return josephus(n,k,next,i+1,killed)


print("Enter n and k: ")
n,k = map(int,input().split())
print("Survivor: ",josephus(n,k,1,1))