class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
        
    def insert_at_beg(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head.prev=node
        self.head=node

    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        itr=self.head   
        while itr.next:
            
            itr=itr.next
        itr.next=node
        node.prev=itr
    def insert_at_index(self,data,index):
        node=Node(data)
        count=0
        if count==index:
            self.insert_at_beg(data)
            return
        if index > self.get_length()+1 or index<0:
            raise Exception("invalid index")
        itr=self.head
        while itr:
            
            if count==index-1:
                node.next=itr.next
                node.prev=itr
                itr.next.prev=node
                itr.next=node
                break
            count+=1
            itr=itr.next
    
    def insert_after_data(self,data):
        node=Node(data)
        
        itr=self.head
        while itr:
            if itr.data==data:            
                node.next=itr.next
                node.prev=itr
                itr.next=node
                itr.next.prev=node
                return
            itr=itr.next
        if itr is None:
            print(data,"doesnt exist in the linked list")
                
    def delete_at_beg(self):
        itr=self.head
        self.head=self.head.next

    def delete_at_end(self):
        if self.get_length()==1:
            self.delete_at_beg()
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.prev.next=None
        itr.prev=None

    def delete_at_index(self,index):
        if index==0:
            self.delete_at_beg()
            return
        if index==self.get_length()-1:
            self.delete_at_end()
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next.prev=itr.prev
                itr.prev.next=itr.next
                break
            itr=itr.next
            count+=1



        

    



        
    def get_length(self):
        count=0
        itr=self.head 
        while itr:
            count+=1
            itr=itr.next
        return count  
    def print(self):
        ll=''
        itr=self.head
        if self.head is None:
            print("List is Empty")
        while itr is not None:
            ll+=str(itr.data)+"-->"
            
            itr=itr.next
        print(ll)

ll=DoublyLinkedList()

ll.insert_at_beg(15)
ll.insert_at_end(13)
ll.insert_at_end(3)
ll.insert_at_beg(25)
ll.insert_at_beg(35)
ll.insert_at_end(43)
ll.insert_at_end(31)
ll.insert_at_beg(56)

ll.insert_at_index(5,2)
ll.insert_after_data(24)
ll.print()
ll.delete_at_beg()
ll.print()
ll.delete_at_end()
ll.print()
ll.delete_at_index(3)
ll.print()