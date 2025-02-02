import numpy as np
def countingSort(A,n:int,k:int):
    #Creamos el arreglo C
    C=np.zeros(k+1,dtype=np.int32)
    B=np.zeros(n,dtype=np.int32)
    #Sumamos las veces que aparece un numero de A
    for i in range(0,len(A)):
        C[A[i]]=C[A[i]]+1
    
    print("Arreglo C")    
    print(C)
    #Ahora hacemos la frecuencia acumulada para C
    for j in range (1,len(C)):
        C[j]=C[j-1]+C[j]
    for j in range (0,len(C)):
        C[j]=C[j]-1
    #Organizamos A en el arreglo B
    print("Arreglo C acumulado")  
    print(C)
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]]=A[i]
        C[A[i]]=C[A[i]]-1
    print("Arreglo B:")  
    print(B)

#arrA=np.array([2,5,3,0,2,3,0,3])
arrA=np.random.randint(0,6,8)
print(arrA)
countingSort(arrA,len(arrA),5)
      