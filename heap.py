import numpy as np
class heap:
    def __init__(self,size):
        self.arr=np.random.randint(0,21,size)
        self.size=size
        self.heapSize=size
    def showArr(self):
        print("[",end="")
        for i in self.arr:
            print(i,end=",")
        print("]")
    def getHeapSize(self):
        return self.heapSize
    
            
        