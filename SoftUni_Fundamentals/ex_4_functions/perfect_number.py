# Python 3 program for aliquot sum

# Function to calculate sum of
# all proper divisors
def aliquotSum(n):
    sm = 0
    for i in range(1, n):
        if (n % i == 0):
            sm = sm + i
    if sm == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


# Driver Code
n = int(input())
aliquotSum(n)
# This code is contributed by Nikita Tiwari.
