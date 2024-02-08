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
    
    def get(self,index):
        if index==-1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current
            
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        if self.length==0:
            return None
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=None
            self.tail=temp
        self.length-=1
        return popped_node
    
    def remove(self,index):
        if index < -1 or index >= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==-1 or index == self.length-1:
            return self.pop()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
    
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def reverse(self):
        prev_node=None
        current=self.head
        while current is not None:
            next_node=current.next
            current.next=prev_node
            prev_node=current
            current=next_node
        self.head,self.tail=self.tail,self.head
        
    def find_middle(self):
        if self.length%2==0:
            i=self.length//2
            middle=self.get(i)
        else:
            i=self.length//2
            middle=self.get(i)
        return middle.value
    
    def remove_duplicates(self):
        current=self.head
        result=[]
        while current:
            if current.value not in result:
                result.append(current.value)
            current=current.next
        self.delete_all()
        for num in result:
            self.append(num)
            
        
                            
                        
        
linked_list=LinkedList()
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
linked_list.prepend(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
print(linked_list)
# linked_list.insert(2,20)
# print(linked_list)
# linked_list.traverse()
# print(linked_list.set_value(-2,90))
# print(linked_list.pop_first())
# print(linked_list.remove(-1))
# linked_list.delete_all()
# print(linked_list)
# linked_list.reverse()
# print(linked_list)
# print(linked_list.find_middle())
linked_list.remove_duplicates()
print(linked_list)