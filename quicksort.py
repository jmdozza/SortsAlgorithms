import numpy as np
def partition(A,p,r):
    #Elegimos un pivote
    pivot=A[r]
    #i inicia una posicion antes de la primera posicion del array
    i=p-1
    for j in range(p,r):
        if(A[j]<=pivot):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=pivot,A[i+1]
    return i+1
    
        

def quicksort(A,p,r):
    #Si p<r significa que hay mas de un elemento
    if(p<r):
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

arr=np.random.randint(0,31,10)
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)