class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_List:
    def __init__(self,data=[]):
        self.ld=len(data)
        self.l=0
        self.head=Node(None)
        
        if self.ld==1:
            self.insert_at_beginning(data[0])
            
            
        elif self.ld>1:
            # self.head.data=data[0]
            # self.head.next=Node(data[1])
            self.l=self.ld
            for i in range(self.ld):
                self.insert_at_index(data[i],i)
                self.l-=1
    
            
    def insertfirst(self,val):
        new_node=Node(val)
        self.head=new_node
        self.l+=1
        
    def insert_at_beginning(self,val):
        if not self.l:
            self.insertfirst(val)
        else:
            new_node=Node(val)
            new_node.next=self.head
            self.head=new_node
            self.l+=1
        
    def insert_at_end(self,val):
        if not self.l:
            self.insertfirst(val)
        else:
            new_node=Node(val)
            current_node=self.head
            while current_node.next!=None:
                current_node=current_node.next
            current_node.next=new_node
            self.l+=1
        
    def insert_at_index(self,val,i):
        if i>=0 and i<=self.l:
            if i==self.l:
                self.insert_at_end(val)
            elif not i:
                self.insert_at_beginning(val)
            else:
                new_node=Node(val)
                current_node=self.head
                j=1
                while j!=i: 
                    current_node=current_node.next
                    j+=1
                new_node.next=current_node.next
                current_node.next=new_node
                self.l+=1
        else:
            print("out of range index while insertion at index function")    
    
    def update(self,val,i):
        if i>=0 and i<self.l:
            current_node=self.head
            j=0
            while j!=i:
                current_node=current_node.next
                j+=1
            current_node.data=val
        else:
            print("out of range index")
            
    def remove_first_node(self):
        if self.l:
            self.head=self.head.next
            self.l-=1
        else:
            print("the linked list is empty!")
                
    def remove_last_node(self):
        if self.l:
            current_node=self.head
            prev_node=Node(None)
            while current_node.next!=None:
                prev_node=current_node
                current_node=current_node.next
                
            if prev_node.next==None:
                self.head=None
                
            prev_node.next=None
            self.l-=1
        else:
            print("the linked list is empty!")
            
            
            
    def remove_at_index(self,i):
        if self.l:
            if i>=0 and i<self.l:
                if i==0:
                    self.remove_first_node()
                elif i==self.l-1:
                    self.remove_last_node()
                else:
                    current_node=self.head
                    prev_node=Node(None)
                    j=0
                    while j!=i:
                        prev_node=current_node
                        current_node=current_node.next
                        j+=1
                    prev_node.next=current_node.next
                    current_node.next=None
                    self.l-=1
            else:
                print("out of range index")
        else:
            print("the linked list is empty!")
    
    def get_val(self,i):
        current_node=self.head
        j=0
        while j!=i:
            current_node=current_node.next
            j+=1
        return current_node.data
       
    def show(self):
        current_node=self.head
        if current_node==None:
            print("no elemnts in the linked list!")
            return
        while current_node.next!=None:
            print(str(current_node.data)+" connected to "+str(current_node.next.data))
            current_node=current_node.next
        if current_node.data!=None:
            print(str(current_node.data)+" connected to None")


