#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

import math  #note: your code should not import modules other than math
default_tol= 1e-15

""" 
    complete each of the following functions to approximate the value of pi. 

    Note: your function should return the estimated value of pi, and the number of terms 
    needed to reach the given accuracy (tol).

    you can use either for loop or while loop, complete each of the following functions
"""
DEBUG = True

def  pi_pow2(tol=default_tol):     #this is for formula (1),  pow of order 2
    pi = 0
    i = 0
    term = 1
    while(term > tol):
        i += 1
        term = 1 / (i ** 2)
        pi += term
        if DEBUG:
            if i > 32000000:
                print("This didn't work")
                break
    result = (pi * 6) ** 0.5
    return (result, i)
    
def  pi_pow2_2(tol=default_tol):   #this is for formula (2),  another formula for pow of order 2
    pi = 0
    i = 0
    term = 1
    while (term > tol):
        i += 1
        term = 1 / (((2 * i) - 1) ** 2)
        pi += term
        if DEBUG:
            if i > 16000000:
                print("This didn't work")
                break
    result = (pi * 8) ** (1/2)
    return (result, i)


def  pi_pow3(tol=default_tol):   #this is for formula (3),  pow of order 3
    pi = 0
    i = 0
    term = 1
    while (abs(term) > tol):
        i += 1
        term = ((-1) ** (i - 1)) / (((2 * i) - 1) ** 3)
        pi += term
        if DEBUG:
            if i > 51000:
                print("This didn't work")
                break
    result = (pi * 32) ** (1/3)
    return (result, i)

    

def  pi_pow4(tol=default_tol):     #this is for formula (4),  pow of order 4
    pi = 0
    i = 0
    term = 1
    while(term > tol):
        if DEBUG:
            if i > 5700:
                print("This didn't work")
                break
        i += 1
        term = 1 / (i**4)
        pi += term
    result = (90 * pi) ** (1/4)
    return (result, i)

    

def  pi_pow4_2(tol=default_tol):   #this is for formula (5),  another pow of order 4
    pi = 0
    i = 0
    term = 1
    while(term > tol):
        if DEBUG:
            if i > 3000:
                print("This didn't work")
                break
        i += 1
        term = 1 / (((2 * i) - 1) ** 4)
        pi += term
    result = (pi * 96) ** (1/4)
    return (result, i)

    

def  pi_pow5(tol=default_tol):     #this is for formula (6),  pow of order 5
    pi = 0
    i = 0
    term = 1
    while (abs(term) > tol):
        if DEBUG:
            if i > 600:
                print("This didn't work")
                break
        i += 1
        term = ((-1) ** (i - 1)) / (((2 * i) - 1) ** 5)
        pi += term
    result = (pi * (1536 / 5)) ** (1/5)
    return (result, i)


    
def  pi_pow6(tol=default_tol):     #this is for formula (7),  pow of order 6
    pi = 0
    i = 0
    term = 1
    while(term > tol):
        if DEBUG:
            if i > 200:
                print("This didn't work")
                break
        i += 1
        term = 1 / (((2 * i) - 1) ** 6)
        pi += term
    result = (960 * pi) ** (1/6)
    return (result, i)


    

def  pi_pow12(tol=default_tol):    #this is for formula (8),  pow of order 12
    pi = 0
    i = 0
    term = 1
    while(term > tol):
        if DEBUG:
            if i > 25:
                print("This didn't work")
                break
        i += 1
        term = 1 / (i ** 12)
        pi += term
    result = (pi * (105 / 691) * (math.factorial(13) / (2 ** 10) )) ** (1/12)
    return (result, i)



    
    
#===================================================================================
#  in any of the functions above, you are not allowed to use the built-in pi value
#  such as math.pi or numpy.pi, the built-in pi can only be used to check accuracy
#  as in the code below.    
#
#  do not change the code below this line    
#===================================================================================
#
from  timeit  import  default_timer

def accuracy_check(pi_func, nterm, tol=1e-10):

    tstart = default_timer()

    pi, n = pi_func(tol=tol)  #observe this interface, it means the 1st output of your function should be pi
    
    tend = default_timer() - tstart
    
    print("\n\nAccuracy check for {}".format(pi_func))
    print("  your returned pi = {},  computed using {} terms of sum, in {:.7f} seconds".format(pi, n, tend))
    error = abs(math.pi - pi)
    print("  error = |math.pi - pi| ={}".format(error))

    if abs(n - nterm) >= 3:
        print('  your # of terms is {}, should be {} plus/minus at most 2'.format(n, nterm))
    else:
        print('  your # of terms is {}, target is {}'.format(n, nterm))
        
    if error > tol**0.5:
        print('***** Test failed: wrong value of pi from {}'.format(pi_func))
    elif error > tol*10:
        print('Test barely passed, likely due to the inefficiency in the summing formula, not due to your code implementation')
    else:
        print('Test passed for {}'.format(pi_func))

        
#==========================================================================
if __name__=='__main__':

    pi_functions = [pi_pow2, pi_pow2_2, pi_pow3, pi_pow4, pi_pow4_2, pi_pow5, pi_pow6, pi_pow12]
    nterms = [31622777, 31622777, 50001, 5624, 2813, 501, 159, 18]
    
    for (pi_fun, nt) in zip(pi_functions, nterms):
        accuracy_check(pi_fun, nt, tol=default_tol)
