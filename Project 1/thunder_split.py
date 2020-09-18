#
# name:Charles Patterson 
# email: cjpatterson@smu.edu
#

import math as m

def is_thunder_split(n):
    """decide if the input integer n is a thunder-split number or not, 
       return True if yes, False otherwise.
       also, print out using the specified format when n is a thunder-split number.
    """

    nstr = str(n)
        
    #hint of the solution: loop over range(1,len(nstr)), get two integers at each step 
    #and determine if n is a  thunder-split number or not. 
    #(another hint: for the printout, you may need to use str in order to show the leading 0's)
    #
    #(add code below to finish this part)
    
    half = len(nstr) // 2
    str1 = nstr[0:half]
    str2 = nstr[half:]
    int1 = int(str1)
    int2 = int(str2)
    if( ( ( int1 + int2 ) ** 2 ) == n):
        print(nstr.rjust(9), "can be thunder-split as (", str1.ljust(10), "+", str2.ljust(10), ")**2")
        return True
    
    half = m.ceil(len(nstr) / 2)
    str1 = nstr[0:half]
    str2 = nstr[half:]
    int1 = int(str1)
    int2 = int(str2)
    if( ( ( int1 + int2 ) ** 2 ) == n):
        print(nstr.rjust(9), "can be thunder-split as (", str1.ljust(10), "+", str2.ljust(10), ")**2")
        return True
    return False
    
def thunder_split_num(b, a=10):
    """find and return all the thunder-split integers in [a,b], store them in a list 
       (order the numbers in increasing order, you don't need to sort if you add the smaller
        number first).  return this list at the end of this function"""
    ts_int=[]    
    ##add code below to finish the task 
    for i in range(a,b+1):
        if(is_thunder_split(i)):
            ts_int.append(i)

    return ts_int

def thunder_split_num_fast(b, a=10):
    """faster way to find and return all the thunder-split integers in [a,b], 
       store them in a list.  return this list at the end """
    ts_int=[]  
    ##add code below to finish the task
    start = m.floor(a ** (1/2))
    if start < 4:
        start = 4
    end = m.ceil(b ** (1/2))
    for i in range(start,end):
        if(is_thunder_split(i**2)):
            ts_int.append(i**2)
    return ts_int

if __name__=='__main__':

    import time

    #correctness tests:
    tList1 = thunder_split_num(10**4, a=110)
    tList2 = thunder_split_num(10**6, a=10*5)
    print(tList1, tList2)
    if tList1==[2025, 3025, 9801, 10000] and tList2[-2:-5:-1]==[998001, 494209, 88209]:
        print("\n nice!   passed initial test \n")
    else:
        print("\n ******* failed initial test ******* \n")

    
    t0 = time.time()
    a=10; bsmall = 10**7
    print("this may take quite a while to run...")
    tList3 = thunder_split_num(bsmall, a)
    print('thunder_split_numbers found: {}'.format(tList3))
    tslow = time.time()-t0
    print('Found thunder split unumbers on [{},{:e}]: seconds used={}'.format(a, bsmall, tslow))

    
    b=10**9
    t0 = time.time()
    tList4 = thunder_split_num_fast(b, a)
    print(tList4)
    if tList4[:len(tList3)]==tList3 and tList4[-5:]==[60481729,99980001,100000000,300814336,493817284]:
        print('thunder_split_numbers found: {}'.format(tList4))
        tfast = time.time()-t0
        print('Fast version on [{},{:e}]: seconds used= {}\n'.format(a, b, tfast))
        if tfast < 2:
            print("\n  Great!!! You solved the bonus problem perfectly!!! \n")
        elif tfast < 10:
            print("\n  Great! You solved the bonus problem, although not as fast. \n")
        else:
            print("\n  Code too slow for the bonus problem, something likely not right. \n")