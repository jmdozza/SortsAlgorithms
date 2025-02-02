import numpy as np
'''Este es el metodo modificado de counting sort
para llevar a cabo el radixsort'''

def countingSortModified(A,digit:int):
    #Creamos el arreglo C
    C=np.zeros(10,dtype=np.int32)
    B=np.zeros(len(A),dtype=np.int32)
    #Sumamos las veces que aparece un numero de A
    for i in range(0,len(A)):
        index=A[i]//10**digit
        C[index%10]+=1
    
    #Ahora hacemos la frecuencia acumulada para C
    for j in range (1,len(C)):
        C[j]=C[j-1]+C[j]
    for j in range (0,len(C)):
        C[j]=C[j]-1
    #Organizamos A en el arreglo B
    
    for i in range(len(A)-1,-1,-1):
        index=A[i]//10**digit
        B[C[index%10]]=A[i]
        C[index%10]-=1
    
    for i in range(0,len(A)):
        A[i]=B[i]