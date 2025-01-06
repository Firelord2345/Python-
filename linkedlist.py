# Here we are implementing the linked list
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def insert_node(self,value,position):
        count=0
        current_node=self.head
        node=Node(value)
         # If the list is empty, insert at the head
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
            return

        # If inserting at the end (position >= length)
        if position >= self.length:
            self.tail.next = node
            self.tail = node
            self.length += 1
            return
        
        if position==0:
            node.next=self.head
            self.head = node
            self.length += 1
            return
            
        while(current_node ):
            if count==position-1:
                node.next=current_node.next
                current_node.next=node
                
                break
            current_node=current_node.next
            count+=1
        self.length+=1
    def display(self):
        current_node = self.head
        while current_node:
            print(f'{current_node.value}->', end="")
            current_node = current_node.next
        print("NULL")
        
    def delete_node(self,position):
        count=0
        if self.head is None:
            return'Empty linked list'
        
        if position >= self.length:
             raise  IndexError("Must delete within the linked list")
        if position==0:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while(current_node):
            if count==position-1:
                current_node.next=current_node.next.next
            current_node=current_node.next
            count+=1
        self.length-=1
    def search(self,value):
       current_node = self.head
       while current_node:
            if current_node.value == value:
                print(True)
                return True
            current_node = current_node.next
       return False
    def reverse(self):
        if self.head is None:
            return'Empty linked list'
        prev_node=None
        current_node=self.head
        next=None
        while current_node.next:
            next=current_node.next
            print(current_node.value)
            current_node.next=prev_node
            prev_node=current_node
            current_node = next
        current_node.next=prev_node
        print(current_node.value)
        temp=self.head
        self.head=self.tail
        self.tail=temp
        return self.display()
    def middle(self):
        if self.head== None:
            return None
        slowptr=self.head
        fastptr=self.head
        while(fastptr and fastptr.next!=None):
            slowptr=slowptr.next
            fastptr=fastptr.next.next
        return slowptr.value
    def n_node_back(self,n):
        count=0
        if self.head== None:
            return None
        mainptr=self.head
        refptr=self.head
        while(count<n):
            
            refptr=refptr.next
            count+=1
        
        while refptr:
            mainptr=mainptr.next
            refptr=refptr.next
        return mainptr
            
        
            
        
        
         
        
        
linkedlist=LinkedList()
linkedlist.insert_node(3,1)
linkedlist.insert_node(2,0)
linkedlist.insert_node(4,2)
linkedlist.insert_node(5,3)
linkedlist.insert_node(7,2)
# linkedlist.delete_node(3)
linkedlist.search(5)
linkedlist.display()
# linkedlist.reverse()

# Calling middle() and displaying the result
middle_value = linkedlist.middle()
if middle_value is not None:
    print(f"The middle value is: {middle_value}")
else:
    print("The list is empty.")
n_node_from_back = linkedlist.n_node_back(2)
if middle_value is not None:
    print(f"The nth  node from back value is: {n_node_from_back.value}")
else:
    print("The list is empty.")
           
            
            
            
    
            
    