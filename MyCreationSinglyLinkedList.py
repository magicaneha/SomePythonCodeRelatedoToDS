class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next 

class LinkedList:
    def __init__(self):
        self.head=None
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_data_at_begining(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
        else:
            itr=self.head
            node=Node(data,None)
            self.head=node
            node.next=itr
    def insert_data_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_at_index(self,index,data):
        if index==0:
            self.insert_data_at_begining()
            return
        if index<0 or index> self.get_length()+1:
            raise Exception("invalid index" )
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1   


        


    def delete_data_at_begining(self):
        if self.head is None:
            print("Linked is empty")
            return        
        self.head=self.head.next
    
    def delete_data(self,data):
        if self.head is None:
            print("Linked is empty")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
    def delete_by_index(self,index):
        if self.head is None:
            print("Linked is empty")
            return
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
            return
        if index==0:
            self.delete_data_at_begining()
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def print(self):
        if self.head is None:
            print("List is Empty")
        itr=self.head
        ll=" "
        while itr:
            ll+=str(itr.data)+"-->"
            itr=itr.next
        print(ll)

            

            
        





ll=LinkedList()
ll.head=Node(13)
ll.insert_data_at_begining(34)
ll.insert_data_at_end(2)
ll.insert_data_at_begining(12)
ll.insert_data_at_end(20)
ll.insert_data_at_begining(32)
ll.insert_data_at_end(35)
ll.insert_data_at_begining(31)

ll.print()
ll.delete_data_at_begining()
ll.print()
ll.insert_data_at_begining(11)
ll.print()
ll.delete_data(32)
ll.print()
ll.insert_at_index(4,48)
ll.print()
ll.delete_by_index(3)

ll.print()
