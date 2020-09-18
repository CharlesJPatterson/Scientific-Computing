#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

def sumDigits(s):
    '''Input s is a string. The returned value should be the sum of all numerical 
       digits in s.  (note, the sum is of int type, not a string)
       In addition, if the first non-empty char of s is a minus sign, then the 
       returned value should add a minus sign to the sum. 
       E.g.,  sumDigits('A33$%4C*+D') should return an integer 10, sumDigits('-+z33$%4-D') 
              and sumDigits('  -A+3-3-4*D') should both return an integer -10.
       That is, minus sign matters only when it is the first non-empty char.
       You may need to look up s.isdigit(), s.lstrip(' ') from help(str).  
     '''
    digits = []
    s = s.lstrip(' ')
    negNum = False
    if (s[0] == '-'):
        negNum = True
    for i in range(len(s)):
        if(s[i].isdigit()):
            digits.append(int(s[i]))
    
    sum = 0
    for i in range(len(digits)):
        sum += digits[i]
    if(negNum):
        sum *= -1
    return sum
            
######################################################################
if __name__=='__main__':

    import numpy as np
    import string, random

    nondigits = string.ascii_letters + '  ' + string.punctuation 

    DEBUG = True
    #DEBUG = False  #uncomment to show more screen output


    ### do not modify code below this line 
    repeat=200
    #arvect=np.random.randn(repeat,1)
    arvect=np.random.normal(10**16, 10**17, (repeat,1))
    arrint=[int(x*10) for x in arvect]

    TEST=[];  tsum={};  ysum={}
    for i in range(len(arrint)):
        if arrint[i] >= 0:
            sloc=0
            for j in str(arrint[i]): 
                sloc+=int(j) #end for j
            tsum[i]=sloc
        else:
            sloc=0
            for j in str(arrint[i])[1:]: 
                sloc+=int(j) #end for j
            tsum[i]=-sloc    #end if 

        s1=str(arrint[i])
        s2=[s1[0]]    
        for j in s1[1:]:
            s2.append(j)
            s2.append(random.choice(nondigits))
        if i%2 == 0:
            s = '      ' + ''.join(s2) 
        else:
            s = '   -/ '  + ''.join(s2) 
            if tsum[i]>0: tsum[i]=-tsum[i]


        if DEBUG: print('s=',s)

        ysum[i]=sumDigits(s)
        if tsum[i] == ysum[i]:
            TEST.append(True)
        else:
            TEST.append(False)  #end for i


    if all(TEST):
        print("\n  Great, you passed {} tests for Problem 3!\n".format(repeat))
    else:
        print("\n *** {} tests failed for Problem 3. Need more debugging.\n".format(len([x for x in TEST if x==False])))
