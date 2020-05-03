#Pseudocode from Algorithms Illumninated: Part 1 by Tim Roughgarden
#-------------------------------------------------------------------------------------
#Karatsuba Pseudocode
#-------------------------------------------------------------------------------------
#Input: two n-digit positive integers x and y
#Output: the produce x*y
#Assumption: n is a power of 2
#-------------------------------------------------------------------------------------
#if n = 1 then
#   compute x*y in one step and return the result
#else
#   a,b := first and second halves of x
#   c,d := first and second halves of y
#   compute p := a+b and q := c+d using grade school addition
#   recursively compute ac := a*c, bd := b*d, and pq := p*q
#   compute adbc := pq-ac-bd using grade school addition
#   compute 10^n*ac+10^n/2*adbc+bd using grade school addition and return the result
#-------------------------------------------------------------------------------------


def karatsubaAlgorithm(x,y):
    pass
