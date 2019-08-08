# Write a recursive function to find the sum of the digits of a number.
def sum_of_digits(n,sum):
    if n <= 0:
        return sum
    sum += n %10
    return sum_of_digits(n//10,sum) 
n = int(input("Enter a number: "))
print("Sum of digits: ",sum_of_digits(n,0))