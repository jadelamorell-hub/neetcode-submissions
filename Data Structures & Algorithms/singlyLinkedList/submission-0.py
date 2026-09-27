class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        #self.values = []

    
    def get(self, index: int) -> int:
        try:
            self.index = self.linked_list[index]
        except IndexError:
            return -1
        return self.index
        

    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0,val)
        #self.value += 1
        

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)
        #self.value += 1
        

    def remove(self, index: int) -> bool:
        try:
            self.linked_list.pop(index)
        except IndexError:
            return False
        #self.value -= 1
        return True

        

    def getValues(self) -> List[int]:
        return self.linked_list

        
