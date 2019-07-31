# Write a recursive function to print all numbers from N to 1 for a given number N.
# tail recursion
def printN(N):
    if N == 0:
        return
    print(N)
    printN(N-1)


# Write a recursive function to print all numbers from 1 to N for a given number N.
#head recursion
def print_one_to_n(N):
    if N == 0:
        return
    
    print_one_to_n(N-1)
    print(N)
#tail recursion
def tailPrint(n,i=1):
    if n == 0:
        return
    print(i)
    tailPrint(n-1,i+1)

N = int(input("Enter N:"))
t = int(input("1. N to 1  or  2. 1 to N (1/2):  "))
if t == 1:
    printN(N)
else:
    tailPrint(N)