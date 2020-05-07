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
    if countDigitsCheck(x,y):
        return x * y
    else:

        x = str(x)
        y = str(y)

        n = (int(len(x)/2))
        m = (int(len(y)/2))

        parts_x = [x[i:i+n] for i in range(0, len(x), n)]
        parts_y = [y[i:i+m] for i in range(0, len(y), m)]

        print(parts_x)
        print(parts_y)

        a,b = int(parts_x[0]), int(parts_x[1])
        c,d = int(parts_y[0]), int(parts_y[1])

        print(a)
        print(b)
        print(c)
        print(d)

    step_one = a*c
    print(step_one)
    step_two = b*d
    print(step_two)
    step_three = (a+b)*(c+d)
    print(step_three)
    step_four = step_three - step_one - step_two
    print(step_four)
    step_five = (step_one*10000)+(step_four*100)+step_two

    return step_five



def countDigitsCheck(one, two):
    count_check_one = countDigits(one)
    count_check_two = countDigits(two)

    if count_check_one == 1 and count_check_two == 1:
        return True
    else:
        return False

def countDigits(number):
    Number = number
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return(Count)





check_function = karatsubaAlgorithm(5678,1234)
test_function = karatsubaAlgorithm(9,9)
print(check_function)
print(test_function)
