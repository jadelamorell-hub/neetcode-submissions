class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        

    
    def get(self, index: int) -> int:
        try:
            self.index = self.linked_list[index]
        except IndexError:
            return -1
        return self.index
        

    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0,val)
        
        

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)
       

    def remove(self, index: int) -> bool:
        try:
            self.linked_list.pop(index)
        except IndexError:
            return False
        
        return True

        

    def getValues(self) -> List[int]:
        return self.linked_list

        
