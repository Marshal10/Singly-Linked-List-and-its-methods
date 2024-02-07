class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next:
                result+=" -> "
            temp_node=temp_node.next
        return result
        
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        
    def insert(self,index,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        
    def traverse(self):
        temp_node=self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node=temp_node.next
            
    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value==target:
                return index
            current=current.next
            index+=1
        return -1
            
                
                        
        
linked_list=LinkedList()
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
linked_list.prepend(40)
linked_list.prepend(10)
linked_list.append(50)
print(linked_list)
linked_list.insert(2,20)
print(linked_list)
# linked_list.traverse()
print(linked_list.search(50))