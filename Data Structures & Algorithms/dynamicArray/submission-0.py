class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dyarr = [None] * capacity
       


    def get(self, i: int) -> int:
        if self.dyarr[i] != None:
            return self.dyarr[i]
        


    def set(self, i: int, n: int) -> None:
        self.dyarr[i] = n


    def pushback(self, n: int) -> None:
      self.index_insert = self.getSize()
      self.arrayLen = self.getCapacity()
      
      if self.arrayLen == self.index_insert:
        self.resize()
        self.arrayLen = self.getCapacity

      if self.arrayLen != self.index_insert:
        self.dyarr[self.index_insert] = n
     

      '''if None in self.dyarr:
        self.dyarr[self.index_insert] = n
        for i in range(0,len(self.dyarr)):
          if i != None:
            self.dyarr[i] = n
        print("None is here")
        for i in self.dyarr:
        if i == None:
         self.dyarr.append(n)'''
     

      


    def popback(self) -> int:
      if(self.getSize() > 0):
        self.last_element = self.dyarr[self.getSize()-1]
        self.dyarr[self.getSize() - 1] = None
      return self.last_element
  

    def resize(self) -> None:
      #self.capacity = self.getCapacity() 
      #if self.capacity == 0:
        #self.capacity = self.getSize()
      for i in range(0,self.getCapacity()):
        self.dyarr.append(None)
      


    def getSize(self) -> int:
      count = 0
      for i in self.dyarr:
        if i == None:
          count += 1
      
      self.size = len(self.dyarr) - count
      
      return self.size
        
    
    def getCapacity(self) -> int:
      self.len = len(self.dyarr)
      return self.len