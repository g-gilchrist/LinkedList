#-----------------------------------------            
#  Node Class
#-----------------------------------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        
#-----------------------------------------            
#  Linked List Class
#-----------------------------------------

class LinkedList:
    def __init__(self):
        self.head = None
     
    #-----------------------------------------            
    #  Add Node to end of Doubly Linked List         
    #-----------------------------------------
                         
    def append(self,data):
        newNode=Node(data)
        if self.head == None:
            newNode.prev = None
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None
 
            
    #-----------------------------------------            
    #  Add Node to begining of Doubly Linked List         
    #-----------------------------------------
                          
    def prepend(self,data):
        newNode=Node(data)
        if self.head == None:
            newNode.prev = None
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
                    

    #-----------------------------------------            
    #  Add Node to Singyly Linked List         
    #-----------------------------------------
       
    def add(self,data):             
        newNode=Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            
    #-----------------------------------------            
    #  Delete Node from LL Class         
    #-----------------------------------------   
    # It is easier to overwrite a node then to delete it, we keep all the pointers in tact & and node is removed.
    # Pyhton's automatic garbage collection will remove the unused node.
 
    def delete(self,data):
        current = self.head 
        if current.data == data:
            self.head = current.next
            return
        while current:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next
            
            
    #-----------------------------------------            
    #  Destructor Function of LL Class         
    #-----------------------------------------
    # Calling this fucntion will remove all nodes.

    def destructor(self):
        current = self.head
        while self.head != None:
            current.next = None
            if current.next == None:
                self.head = None
                
                
    #-----------------------------------------            
    #  Prints Specific node of LL Class         
    #-----------------------------------------               
    def search(self,data):
        current = self.head 
        if current.data == data:
            print(current.data)
            return
        while current:
            if current.data == data:
                print(current.data)
                break
            current = current.next
            
        
    #-----------------------------------------            
    #  Prints all nodes of LL Class         
    #-----------------------------------------

    def printNodes(self):
        current = self.head
        while current != None:
            print(current.data)
            current=current.next

            
#-----------------------------------------            
#  Main       
#-----------------------------------------            

LL = LinkedList()

LL.append('Node1')
LL.append('Node2')
LL.prepend('Node3')

LL.printNodes()

