# Write a program that generates all odd numbers from 1 to n.
# Set n in the beginning of the program and use a while loop to compute the numbers.
# (Make sure that if n is an even number, the largest generated odd number is n-1)

n = 1
if n % 2 == 0:
    n -= 1
while n <= 100:
    print(n)
    n += 2