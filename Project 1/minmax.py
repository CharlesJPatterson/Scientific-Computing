#
# Charles Patterson | cjpatterson@smu.edu 
#
#===========================================================

def  min_and_max(alist):
    '''The input alist is a list of numeric type, find the min and max as well as the 
       positions of min and max of the list,  return them as 
       ((min, id_of_min),  (max, id_of_max)).
       Requirements: 1. All position counts should start from 1, not 0;  
       2. When min or max is unique, the returned id should be a scalar, not a list;
          When min or max are non-unique, the returned id should be a list containing all min or max ids.

       E.g.,  calling    (a, ida), (b, idb) = min_and_max([3, 5, 7, 1, 2, 7, 7, 6]) 
       should obtain  (a, ida)=(1, 4),  (b, idb)=(7, [3, 6, 7]), 
       Note 1:  the position count starts with 1, not 0.
       Note 2:  try the above simple example first,  make sure your code returns (a, ida)=(1, 4),
                (a, ida) should not be any of these  (1, 3), (1, [3]), or (1, [4]);
                and (b, idb) should not be (7, [2, 5, 6]).
    '''
    min = alist[0]
    max = alist[0]
    for i in range(1, len(alist)):
        if (min > alist[i]):
            min = alist[i]
        if (max < alist[i]):
            max = alist[i]
    MinList = []
    MinPos = []
    MaxList = []
    MaxPos = []
    for i in range(len(alist)):
        if(alist[i] == min):
            MinList.append(alist[i])
            MinPos.append(i+1)
        if(alist[i] == max):
            MaxList.append(alist[i])
            MaxPos.append(i+1)
    if (len(MinList) == 1):
        id_of_min = MinPos[0]
    else:
        id_of_min = MinPos
    if (len(MaxList) == 1):
        id_of_max = MaxPos[0]
    else:
        id_of_max = MaxPos
    
    return ((min, id_of_min),  (max, id_of_max))

############################################################################
#do not modify code below this line
if __name__=='__main__':

    import random, math
    import numpy as np

    # alist = [3, 5, 7, 1, 2, 7, 7, 6]
    # (a, ida), (b, idb) = min_and_max(alist) 
    # print(a, ida);  print(b, idb)

    Tests=[]; repeat=30
    for iter in range(repeat):  #run 10 times
        alist=[]
        for i in range(300): 
            alist.append(random.gauss(0,10))
            if i%3 ==0 and i>2:
                alist.append(alist[i-1]); alist.append(alist[i-2]) #end 'for i'

        ##call min_and_max() function  (you do not need to change anything)
        ((min, id_of_min),  (max, id_of_max)) = min_and_max(alist)

        ##call some external functions for verification
        np_min = np.min(alist);   np_max=np.max(alist)
        id_min = np.where(alist == np_min);  id_max=np.where(alist == np_max)

        test=True
        if min != np_min:   print('min value error');  test=False
        if max != np_max:   print('max value error');  test=False

        if len(id_min[0])==1:
            if  id_of_min != id_min[0][0]+1: 
                print('min index error');  
                test=False  #end 'if id'
        else:
            for i in range(len(id_min[0])):
                if id_of_min[i] != id_min[0][i]+1:
                    print('min index error');  
                    test=False   #end 'if len()'

        if len(id_max[0])==1:
            if  id_of_max != id_max[0][0]+1: 
                print('min index error');  
                test=False       #end 'if id_'
        else:
            for i in range(len(id_max[0])):
                if id_of_max[i] != id_max[0][i]+1:
                    print('min index error');  
                    test=False   #end  'if len()'  


        Tests.append(test)
        print("Run test {},  pass is {}".format(iter, test))
        print("\tyour min is {:.5f},  np_min is {:.4f}".format(min, np_min))
        print("\tyour id_min={},  it should be id_min={}".format(id_of_min, id_min[0]+1))
        print("\tyour max is {:.5f},  np_max is {:.5f}".format(max, np_max))
        print("\tyour id_max={},  it should be id_max={}".format(id_of_max, id_max[0]+1))

    if all(Tests[:]):
        print("\nCongratulations, you passed all {} tests for Problem 2!".format(repeat))
    else:
        print("\n\t***** Some or all tests failed, need further debugging for this problem\n\n")
