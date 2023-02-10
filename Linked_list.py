class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node= Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    #Take a lis of values and create a fresh linked list
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next    
        return count

    def remove_at(self,index):
        if index <0 or index>= self.get_length():
            print ("Invalid index")
            return
        if index==0:
            self.head= self.head.next
            return
        count=0
        itr=self.head
        while itr:
            
            if count == index-1 :
                itr.next= itr.next.next
                break
                
            itr=itr.next
            count += 1

    #def remove_by_value(self, data):

    
    def insert_at(self,index,data):
        if index<0 or index >self.get_length():
            print("invlaid index")
        if index ==0:
            self.insert_at_begining(data)
        if index == self.get_length():
            self.insert_at_end(data)
        count =0
        itr=self.head
        while itr:
        
            if count==index-1:
                
                node= Node(data,itr.next)
                itr.next= node
                break
            itr=itr.next
            count+=1
    def insert_after_value(self, data_after, data_to_insert):
        count=0
        itr=self.head
        while itr:
            count+=1
            if itr.data==data_after:
                
                node=Node(data_to_insert,itr.next)
                itr.next=node
                break                       
            itr=itr.next
        if count==self.get_length():
                print(data_after ,"doesnt exist" ) 
          
    def remove_by_value(self,data):
        count=0
        itr=self.head
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next

        while itr:
            count+=1
            if itr.next.data==data and count!= self.get_length():
                itr.next=itr.next.next
                break
            else:
                print(data,"doesnt exist")
                break
            itr=itr.next
        
                
    def print(self):
        if self.head is None:
            print ("Linked list is empty")
            return
        itr= self.head
        llstr=' '
        while itr:
            llstr += str(itr.data)+ '--->'
            itr=itr.next
        print(llstr)

    
        


    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

    #
    # Remove first node that contains data

if __name__=='__main__':
    ll=Linked_list()
    #ll.insert_at_begining(5)
    
    #ll.insert_at_end(67)
    #ll.insert_at_begining(10)
    ll.insert_values(["bana","apple","mango","strawbeery","raspberry"])
    ll.print()
    #ll.remove_at(1)
    #ll.print()
    #ll.insert_after_value("apple1","peach")
    ll.remove_by_value("applqe")
    ll.print()