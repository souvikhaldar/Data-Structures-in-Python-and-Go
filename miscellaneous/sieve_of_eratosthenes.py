# Sieve of Eratosthenes is used to optimally find the all the prime numbers till the 
# provided upper bound (say n). The time complexity of this algorithm is O(n.loglogn)
import math
n = int(input("Enter the upper bound:"))
# first we assume all numbers in the given range are prime
prime = {}
for i in range(2,(n+1)):
    prime[i] = True
# mark all multiples of this prime number as non-prime (since they can be divided by this number)
for val in range(2,int(math.sqrt((n+1)))):
    if (prime[val] == True):
        j = 2
        while ((val*j)<= (n+1)):
            prime[val*j] = False
            j +=1
for p in prime.keys():
    if prime[p]== True:
        print(p)
       
