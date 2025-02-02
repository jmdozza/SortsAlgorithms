import math as mt
import numpy as np
def merge(A,low,mid,high):
    lenL=mid-low+1
    lenR=high-mid
    print("len L=",lenL)
    print("len R=",lenR)
    L=np.zeros(lenL,dtype=np.int64)
    R=np.zeros(lenR,dtype=np.int64)
    #Se pasan los valores de A a L y R
    for i in range(0,lenL):
        L[i]=A[i+low]
    for j in range(0,lenR):
        R[j]=A[j+mid+1]
    #Se inicializan las variables que iteran sobre L y R
    i=0
    j=0
    k=low #Aca es donde se debe empezar a escribir en el arreglo A
    while(i<lenL and j<lenR):
        if(L[i]<=R[j]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    #Dos ciclos while en caso de que queden elementos sobrantes en L o R
    #Para L
    while(i<lenL):
        A[k]=L[i]
        i+=1
        k+=1
    while(j<lenR):
        A[k]=R[j]
        j+=1
        k+=1
    
    
def mergeSort(A,low,high):
    if (low>=high):
        return
    mid=mt.floor((low+high)/2)
    mergeSort(A,low,mid)
    mergeSort(A,mid+1,high)
    merge(A,low,mid,high)

arr=np.array([12,3,7,9,11,16,1,22,5])
loww=0
high=len(arr)-1
mergeSort(arr,loww,high)
print(arr)
        