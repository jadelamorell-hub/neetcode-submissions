class LinkedList:
    
    def __init__(self):
      self.head = None
    
        

    
    def get(self, index: int) -> int:
    
        current_node = self.head
        current_index = 0
        while current_index != index and current_node != None:         
          current_node = current_node.next
          current_index += 1

        if current_node == None:
          return -1
        else:
          return current_node.data
          
      
        
        

    def insertHead(self, val: int) -> None:
      new_node = Node(val)
      new_node.next = self.head
      self.head = new_node
      

        

    def insertTail(self, val: int) -> None:
      new_node = Node(val)
      if self.head == None:
        self.head = new_node
      else:
        current_node = self.head
        #traverse the nodes to find last node
        while current_node.next != None:
          current_node = current_node.next
        current_node.next = new_node

        
        

    def remove(self, index: int) -> bool:
        current_node = self.head
        prev_node = None
    
        current_index = 0
        while current_index != index and current_node != None:  
          prev_node = current_node       
          current_node = current_node.next
          current_index += 1

        if current_node == None:
          return False
        else:      
          if prev_node != None:
            prev_node.next = current_node.next
          elif prev_node == None:
            self.head = current_node.next
          return True

          '''if current_node.next != None or current_node.next == None:
            if prev_node != None:
                prev_node.next = current_node.next
              else:
                self.head = None
                return False'''


      
        

        

    def getValues(self) -> List[int]:
      hold_values = []
      current_node = self.head
     
      while current_node != None:
        hold_values.append(current_node.data)
        current_node = current_node.next
      

      return hold_values

class Node:

      def __init__(self, data):
        self.data = data
        self.next = None
        
