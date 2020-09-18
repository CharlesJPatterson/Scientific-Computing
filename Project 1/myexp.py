# Finished
#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

#you need to update the interface for this myexp() function
def myexp(x, tol=1e-10):  
    ''' For any input x which is a real number, and a given accuracy (tol), 
        compute exp(x) as the sum of Taylor series.
        Return the sum and the number of terms used in the series to reach the accuracy tol.
    '''
    neg = False
    if x < 0:
        neg = True
        x *= -1
    e = 0
    i = 0
    term = 1
    while(abs(term) > tol):
        e += term
        term *= x/(i+1)
        i+=1
    if neg:
        return 1/e, i-1
    return(e,i-1)

#===========================================================
# do not touch the following code
#
if __name__=='__main__':
    import math
    import numpy as np

    err_cnt = 0       #count the # of errors in the function value exp(x)
    indx_err_cnt=0    #count the # of errors in the returned integer of #terms used
    
    nList1_ori = [];
    nList1= [71, 69, 66, 63, 60, 57, 54, 52, 49, 46, 43, 40, 37, 34, 31, 28, 24, 21, 17, 13, 0, 13, 17, 21, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 54, 57, 60, 63, 66, 69, 71]

    print('\n----------- test 1 -----------------\n')
    xvect = np.arange(20.0, -21.0, -1)
    for x in xvect:
        #test using the default tol=1e-10 
        sum, n = myexp(x)
        mathexp = math.exp(x)
        absolute_error = abs(mathexp - sum)
        relative_error = abs(mathexp - sum)/mathexp
        nList1_ori.append(n)
        
        print('exact exp({:6.2f})={:14.10e},  your_exp={:14.10e},  abs_err={:10.5e},  rel_err={:14.10e}'.
              format(x,  mathexp,  sum, absolute_error, relative_error))
        
        if abs(relative_error) > 1e-10:
            err_cnt += 1
            print(' ***** your exp({}) is wrong'.format(x))

    #check the correctness of # of terms used 
    for i in range(len(xvect)):
        if nList1[i] != nList1_ori[i]:
            print(' #terms used for x={} should be {}, you got {}'.format(xvect[i], nList1[i], nList1_ori[i]))
            indx_err_cnt += 1
    
            

    print('\n----------- test 2 -----------------\n')
    nList2_ori = [];
    nList2= [159, 154, 148, 143, 137, 132, 126, 121, 115, 110, 104, 99, 93, 87, 82, 76, 71, 65, 59, 53, 47, 41, 35, 28, 21, 11, 17, 25, 32, 38, 44, 50, 56, 62, 68, 73, 79, 85, 90, 96, 101, 107, 112, 118, 124, 129, 135, 140, 145, 151, 156, 162]
    
    tol = 10**(-12)
    xvect = np.arange(50.5, -52, -2.)
    for x in xvect:
        #test using a specified tol
        s, n = myexp(x, tol)
        mathexp = math.exp(x)
        absolute_error = abs(mathexp - s)
        relative_error = abs(mathexp - s)/mathexp
        nList2_ori.append(n)
        
        print('exact exp({:6.2f})={:14.12e},  your_exp={:14.12e},  abs_err={:10.5e},  rel_err={:14.10e}'.
              format(x,  mathexp,  s, absolute_error, relative_error))
        
        if abs(relative_error) > tol:
            err_cnt += 1
            print(' ***** your exp({}) is wrong'.format(x))        

    for i in range(len(xvect)):
        if nList2[i] != nList2_ori[i]:
            print(' #terms used for x={} should be {}, you got {}'.format(xvect[i], nList2[i], nList2_ori[i]))
            indx_err_cnt += 1    
            
    if err_cnt == 0:
        print('\n Your code passed all tests on function values exp(x)')
    else:
        print('\n ***** Your code failed {} tests on function values'.format(err_cnt))

    if indx_err_cnt == 0:
        print('\n Your code passed all tests on the # of terms used')
        #print('nList1=', nList1_ori)
        #print('nList2=', nList2_ori)
    else:
        print('\n ***** Your code failed {} tests on the # of terms used'.format(indx_err_cnt))       
