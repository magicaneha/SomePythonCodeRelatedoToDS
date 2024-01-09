class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self, data):
        node = Node(data)
        current = self.head
         
        node.next = self.head
 
        if self.head is not None:
            while current.next != self.head:
                current = current.next
            current.next = node
 
        else:
            node.next = node 
 
        self.head = node
    
    def insert_at_end(self,data):
        node=Node(data)
        current=self.head
        if self.head is not None:
            while current.next!=self.head:
                current=current.next
            current.next=node
            node.next=self.head
            return
        else:
            node.next=node
        self.head=node
    
    def remove_at_beg(self):
        if self.head.next==self.head:
            self.head=None
        if self.head is not None:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=self.head.next
            self.head=current.next

    def remove_at_end(self):
        if self.head.next==self.head:
            self.head=None
        if self.head is not None:
            current=self.head
            while current.next.next!=self.head:
                current=current.next
            current.next=self.head    

    def print (self):
        current=self.head
    
        if self.head is not None:
            ll=' '
            while True:
                ll+=str(current.data)+"-->"
                current=current.next
                if current==self.head:
                    break
             
            print (ll)
          
    
myList= CircularLinkedList()
myList.insert_at_beg(5)
myList.insert_at_beg(1)
myList.insert_at_beg(4)
myList.insert_at_end(6)
myList.insert_at_end(2)
myList.print()
myList.remove_at_beg()
myList.print()
myList.remove_at_end()
myList.print()

