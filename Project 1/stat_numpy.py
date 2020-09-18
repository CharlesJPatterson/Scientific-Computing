#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

import numpy as np

def stat_comp(n=100,  mean=1000,  deviation=0.32):
    x = np.random.normal(mean, deviation, n)
    norm1 = np.sum(np.absolute(x))
    norm2 = np.linalg.norm(x)
    
    xbar = 0
    s = 0
    for i in range(len(x)):
        xbar += x[i]
        s += x[i]**2
    xbar *= 1/n
    xbar = xbar ** 2
    sd11 = ( ( (1/n) * s) - xbar) ** (1/2)
    sd12 = np.std(x)
    
    xbar = 0
    for i in x:
        xbar += i
    xbar /= n

    s = 0
    for i in x:
        s += (i - xbar) ** 2

    sd21 = ((1/n) * s) ** (1/2)
    sd22 = np.std(x)
    return x, norm1, norm2, sd11, sd12, sd21, sd22

#===========================================================
# do not change code below this line
def verify(x, norm1, norm2, sd11, sd12, sd21, sd22, mean, devia):

    n = len(x)
    if abs(mean - np.sum(x)/n) > np.sqrt(n)*devia: 
        print('Possible error in construction of x')
        return False
        
    if norm1**2 - norm2**2 < 0:
        print('1st possible error in norms')
        return False

    tol=1e-8
    s = 0.0
    for i in range(n):
        for j in range(i+1, n):
                s += abs(x[i]*x[j]) #end for j for i
    diff = abs(norm1**2 - norm2**2 - 2*s)
    if diff/norm1**2 > tol: 
        print('2nd possible error in norms: relative_diff_norms={:.8e}'.format(diff/norm1**2))
        return False

    if abs(sd11 - sd12) > tol: 
        print('Possible error in sd11 & sd12')
        return False
       
    if abs(sd21 - sd22) > tol: 
        print('Possible error in sd21 & sd22')
        return False

    if abs(sd11 - sd21) + abs(sd12 - sd22) > tol*10:
        print('Possible error in sd11 to sd21')
        return False  #this False might be the least reliable one
       
    return True

#===========================================================
if __name__=='__main__':

    DEBUG=True

    n = 1000
    #try the default mean and deviation
    mean=1000; deviation=0.32
    x, norm1, norm2, sd11, sd12, sd21, sd22 = stat_comp(n)
    if verify(x, norm1, norm2, sd11, sd12, sd21, sd22, mean, deviation):
        print('Test passed\n')
    else:
        print('***** Need further debug.  Possible errors in code*****\n')


    ipass=0; ifail=0
    for mean in range(0, 3000, 200):
        deviation = 0.1+ np.sqrt(mean/10)
        if DEBUG:
            print('mean = {},  deviation={}'.format(mean, deviation))

        x, norm1, norm2, sd11, sd12, sd21, sd22 = stat_comp(n,  mean,  deviation)
        if verify(x, norm1, norm2, sd11, sd12, sd21, sd22, mean, deviation):
            print('Test passed\n');  ipass+=1
        else:
            ifail+=1
            print('***** Need further debug.  Possible errors in code*****\n')


    print("  Total {} test:  Passed {}".format(ipass+ifail, ipass))
    if ifail==0:
        print("  Congratulations, you passed all tests for Problem 7.")