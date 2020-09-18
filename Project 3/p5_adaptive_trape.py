"""
Name: Charles Patterson
email: cjpatterson@smu.edu
"""

import numpy as np
#from scipy.lib.six import xrange
from p4_quadrature import *  #this imports all functions in  p4_quadrature.py

#I went out and learned the Romberg rule because I thought that be easy enough to implement

#--------------------------------------------------------------------
def Trapezoid_adap(f, a, b, tol=1e-5):
    n = 1
    interval = [a,b]
    intrange = b-a
    term = DiffTrap(f, interval, n)
    Inew = intrange * term
    resmat = [[Inew]]
    err = np.inf
    i = 1
    while True:
        n = n * 2
        term = term + DiffTrap(f, interval, n)
        resmat.append([])
        resmat[i].append(intrange * term / n)
        for k in range(i):
            resmat[i].append(RombergDiff(resmat[i-1][k], resmat[i][k], k+1))
        Inew = resmat[i][i]
        Iold = resmat[i-1][i-1]

        err = abs(Inew - Iold)
        rtol = max(abs(Iold), abs(Inew), 0.01)*max(0.5e-10, tol/100)
        if err < tol or err < rtol*abs(Inew):
            break
        i+=1
    return Inew, n

def DiffTrap(f, interval, n):
    if n == 1:
        return 0.5*(f(interval[0])+f(interval[1]))
    
    else:
        numtosum = n/2
        h = float(interval[1]-interval[0])/numtosum
        lox = interval[0] + 0.5 * h
        points = lox + h * np.arange(0, numtosum)
        s = sum(f(points),0)
        return s

def RombergDiff(b, c, k):
    tmp = 4.0**k
    return (tmp * c - b)/(tmp - 1.0)

#====================================================================================
#do not modify code below, instead, make interfaces (especially the returns)
#of your functions above fit the function calls below to avoid any mismatch.
#
if __name__=='__main__':   

    import scipy.linalg as LA
    from scipy.integrate import  quad

    f1 = lambda x:  x**5 * np.cos(x) 
    a =0.0;  b=np.pi;  tol=3e-7

    #call scipy for verification 
    f_quad, ferr = quad(f1, a, b, epsrel=1e-12)
    print("by scipy:  f_quad={},  ferr={}".format(f_quad, ferr))

    n = 10000
    for i in range(1, 11):
        f_trap, pf_trap = NumSum(f1, a, b, n*i, rule='TrapSum')
        print(" Trapezoid: using {} panels,  error={}".format(pf_trap, abs(f_trap - f_quad)))

    if abs(f_trap - f_quad) < 5e-8: 
        print(" Test trapezoidal on f1:  passed !\n")
    else:
        print("\n *********** Test trapezoidal on f1:  failed ***********\n\n")

    n = 1000
    for i in range(1, 11):    
        f_simp, pf_simp = simpson(f1, a, b, n*i, type='1/3')
        print(" Simpson 1/3:  using {} panels,  error={}".format(pf_simp, abs(f_simp - f_quad)))

    if abs(f_simp - f_quad) < 5e-11: 
        print(" Test Simpson on f1:  passed !\n")
    else:
        print("\n *********** Test Simpson on f1:  failed ***********\n\n")

    
    f_trap_adap, pf_trap_adap = Trapezoid_adap(f1, a, b, tol)
    print(" Trapezoid adaptive: using {} panels,  error={}".format(pf_trap_adap, abs(f_trap_adap - f_quad)))
    if abs(f_trap_adap - f_quad) <= 2*tol:
        print(" Test adaptive trapzoidal on f1:  passed !\n")
    else:
        print("\n *********** Test adaptive trapzoidal on f1:  failed ***********\n\n")        



    f = lambda x:  np.sqrt(x)*np.cos(x) 
    g = lambda x:  2*x**2 * np.cos(x**2)
    a = 0.0;  b=np.pi

    f_quad, ferr = quad(f, a, b, epsrel=1e-12)
    g_quad, gerr = quad(g, a, b**(1/2), epsrel=1e-12)
    print("by scipy:   fint={}, ferr={:.3e};  gint={}, gerr={:.3e}".format(f_quad, ferr, g_quad, gerr))
    print("            Note the two integrals should be the same theoretically, but f is much harder")
    print("            to numerically evalueate due to its derivative being infinite at x=0\n")

    n = 5000
    f_trap, fp_trap = NumSum(f, a, b, n*20)
    g_trap, gp_trap = NumSum(g, a, b**(1/2), n*10)
    print("by trapezoid: fint={}, fpanels={},  err={} \n             gint={}, gpanels={}, err={}".
          format(f_trap, fp_trap, abs(f_trap - g_quad),  g_trap,  gp_trap,  abs(g_trap - g_quad) ))
    if abs(f_trap - f_quad) > 1e-5  or abs(g_trap - g_quad) > 1e-6:
        print("\n *********** Test trapzoidal on f & g:  failed ***********\n\n") 
    else:
        print(" Test trapzoidal on f & g:  passed !\n")

    f_simp, fp_simp = simpson(f, a, b, n*4)
    g_simp, gp_simp = simpson(g, a, b**(1/2), n)
    print("by simpson 1/3: fint={}, fpanels={},  err={} \n             gint={}, gpanels={}, err={}".
          format(f_simp, fp_simp, abs(f_simp - g_quad), g_simp, gp_simp, abs(g_simp - g_quad) ))
    if abs(f_simp - f_quad) > 1e-5  or abs(g_simp - g_quad) > 1e-6:
        print("\n *********** Test Simpson on f & g:  failed ***********\n\n") 
    else:
        print(" Test Simpson 1/3 on f & g:  passed !\n")

    tol=1e-7
    f_trap_adap, pf_trap_adap = Trapezoid_adap(f, a, b, tol)
    g_trap_adap, gf_trap_adap = Trapezoid_adap(g, a, b**(1/2), tol)
    print("Trapezoid adaptive on f: using {} panels,  error={}".
          format(pf_trap_adap, abs(f_trap_adap- g_quad)))
    print("Trapezoid adaptive on g: using {} panels,  error={}".
          format(gf_trap_adap, abs(g_trap_adap- g_quad)))

    if abs(f_trap_adap - f_quad) <= 10*tol:
        print(" Test adaptive trapezoidal on f:  passed !\n")
    else:
        print("\n *********** Test adaptive trapezoidal on f:  failed ***********\n\n")        
    if abs(g_trap_adap - g_quad) <= 2*tol:
        print(" Test adaptive trapezoidal on g:  passed !\n")
    else:
        print("\n *********** Test adaptive trapezoidal on g:  failed ***********\n\n")       
