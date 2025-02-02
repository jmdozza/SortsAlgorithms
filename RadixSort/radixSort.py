import numpy as np
from countSortMod import countingSortModified
import math
def radixSort(A):
    maxel=maxElement(A,0,len(A)-1)
    d=getD(maxel)
    for i in range(0,d):
        countingSortModified(A,i)

#Funcion para obtener el elemento mayor
def maxElement(A,p,r):
    if(p==r):
        return abs(A[p])
    else:
        q=math.floor((r+p)/2)
        return max(maxElement(A,p,q),maxElement(A,q+1,r))
        
def getD(numb: int):
    if numb == 0: 
        return 1
    count = 0
    lnumb = abs(numb)
    while lnumb >= 1:
        lnumb = math.floor(lnumb / 10)
        count += 1
    return count

arr=np.array([121,100,51,400,28,15,324])
print(arr)
radixSort(arr)
print(arr)
