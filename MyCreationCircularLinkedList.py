class Node:
     
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class circularLinkedList:
     
    def __init__(self):
        self.head = None
 
    def insert_at_beg(self, data):
        node = Node(data)
        itr = self.head
         
        node.next = self.head
 
        if self.head is not None:
            while(itr.next != self.head):
                itr = itr.next
            itr.next = node
 
        else:
            node.next = node 
 
        self.head = node 

    def print_it(self):
        itr = self.head
        if self.head is not None:
            ll=' '
            while(True):
                ll+=str(itr.data)+"-->"
                itr = itr.next
                if (itr == self.head):
                    break
            print(ll)
 
my_list = circularLinkedList()

my_list.insert_at_beg (56)
my_list.insert_at_beg (78)
my_list.insert_at_beg (12)


my_list.print_it()