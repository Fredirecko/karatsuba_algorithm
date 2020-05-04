#Pseudocode from Algorithms Illumninated: Part 1 by Tim Roughgarden
#-------------------------------------------------------------------------------------
#Karatsuba Pseudocode
#-------------------------------------------------------------------------------------
#Input: two n-digit positive integers x and y
#Output: the product x*y
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
    return(countDigitsCheck(x,y))






def countDigitsCheck(one, two):
    count_check_one = countDigits(one)
    count_check_two = countDigits(two)
    a = one
    b = two
    Karatsuba = "Run Karatsuba Algorithm"
    print(count_check_one)
    print(count_check_two)
    if count_check_one == 1 and count_check_two == 1:
        answer = a * b
        return(answer)
    else:
        return(Karatsuba)



def countDigits(number):
    Number = number
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return(Count)





check_function = karatsubaAlgorithm(100,9)
print(check_function)
