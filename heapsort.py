import math
from heap import heap

#Procedure that obtain i parent
def parent(i):
    return math.floor(i-1/2)
#Procedure that obtain left i subtree
def left(i):
    return 2*i+1
#Procedure that obtain right i subtree
def right(i):
    return 2*i+2

#Procedure that guarantee maxheap property
def maxHeapify(A:heap,ind):
    leftNode=left(ind)-1
    rightNode=right(ind)-1
    largest=ind
    if(leftNode<A.getHeapSize()):
        if(A.arr[leftNode]>A.arr[ind]):
            largest=leftNode
            
    if(rightNode<A.getHeapSize()): 
        if(A.arr[rightNode]>A.arr[largest]):
            largest=rightNode
    if(ind!=largest):
        A.arr[ind], A.arr[largest] = A.arr[largest], A.arr[ind]
        maxHeapify(A,largest)

#Procedure that builds a maxheap  
def builtMaxHeap(A:heap):
    nTam=A.getHeapSize()
    antLeaf=math.floor(nTam/2)
    for i in range(antLeaf-1,-1,-1):
        maxHeapify(A,i)

def heapSort(A:heap,n):
    builtMaxHeap(A)
    for i in range(n-1,0,-1):
        A.arr[0], A.arr[i] = A.arr[i], A.arr[0]
        A.heapSize-=1
        maxHeapify(A,0)
        
    
arrObj=heap(size=11)
arrObj.showArr()
heapSort(arrObj,arrObj.getHeapSize())
arrObj.showArr()
        