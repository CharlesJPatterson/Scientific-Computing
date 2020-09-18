#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

def  reverse_digits(num):
    '''The input num should be an integer, if not, raise an exception and return 
       with some instructive message to input int type data.
       When coded correctly,  
            reverse_digits(12345) and reverse_digits(+12345) should return 54321, 
            and reverse_digits(-12345) should return -54321.
       That is, besides reversion of digits, the signs need some addition attention.
       To avoid complications caused by int() removing leading 0's, such as int(0001)=1,
       you can return the reversed digits as a str, keeping all leading zeros if any.
    '''
    #if type(num) != int:  ##this does not work for numpy.int64  etc
    #     raise  Exception("Input is not an integer.")
    try:
        num=int(num)
    except:
        raise  Exception("Input is not an integer.")    

    
    theNumber = ""
    positive = True
    if (num < 0):
        positive = False
    if(not positive):
        theNumber += '-'
        num *= -1
    
    while(num > 9):
        theNumber += str(num%10)
        num //= 10
    theNumber += str(num)
    return theNumber


    
##do not modify code below this line
####################################################################
def verify(num, revnum):
    #input num is int type, revnum is str type

    sn = str(num);   sinv = str(revnum)
    if sn[0]=='-':
        if sinv[0] != '-':  return False
    
    if sn[0]=='+':
        if not sinv[0].isdigit():  return False
        
    if sn[0]=='-':
        sn = sn[1:];  sinv=sinv[1:]
    elif sn[0]=='+':
        sn = sn[1:]
        
    #use a very elementary method for verification 
    for i in range(len(sn)):
        if sn[i] != sinv[-(i+1)]:  return False

    return True

####################################################################
if __name__=='__main__':

    import numpy as np
    DEBUG = True

    repeat=100

    ##if you use python in window OS, and you get complaint of int32 out of bound,
    ##then you need to reduce the range of numbers to be tested. the following code
    ##will do this automatically for you
    try:
        arynum = np.random.randint(-10**18, 10**18, repeat)
    except:
        arynum = np.random.randint(-10**9, 10**9, repeat)

    TEST=[]
    for num in arynum:
         revnum=reverse_digits(num)
         if DEBUG:
             print('    num={}\n revnum={}'.format(num, revnum))
         TEST.append(verify(num, revnum))

    if all(TEST):
        print("\n  Congratulations, you have passed all {} tests for Problem 4.\n".format(repeat))
    else:
        print("\n *** {} tests failed. Need more debugging.\n".format(len([x for x in TEST if x==False])))


    for num in [+1234500007890000,  -50329320407933661000000,  +66154332782429707000 ]:
        revnum=reverse_digits(num)
        print('the reverse of {} is {}'.format(num, revnum))
        if verify(num, revnum):
            print('Passed')
        else:
            print('Failed, recheck your code')
        
