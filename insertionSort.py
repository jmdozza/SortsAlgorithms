import numpy as np
def insertionSort(A):
    for i in range(1,len(A)):
        temp=A[i]
        j=i-1
        while(A[j]>temp and j>=0):
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp



