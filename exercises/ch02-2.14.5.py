'''
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

A = P (1 + r/n)^(nt)

Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years.
'''

P = 10000
n = 12
r = 0.08

t = float(input("How many years will the money be compounded for? "))

A = P * (1 + r/n) ** (n * t)

print("The final amount is", A, "after", t, "years")