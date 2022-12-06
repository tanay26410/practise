#linked list
#creation of linked list and insertion of linked list

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self) -> None:
        self.head=None
    #add elements at front
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    #add elements in b/w
    def insertbw(self,prev_node,new_data):
        if prev_node is None:
            print('the given previos node must in linked list')
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    #insert in end
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    #print elements
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
# llist.head=Node(1)
# second=Node(2)
# third=Node(3)
# llist.head.next=second
# second.next=third
# Insert 6.  So linked list becomes 6->None
llist.append(6)
 
# Insert 7 at the beginning. So linked list becomes 7->6->None
llist.push(7)
 
# Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.push(1)
 
# Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.append(4)
 
# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertbw(llist.head.next, 8)
 
llist.printlist()


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self) -> None:
        self.head=None
    #add elements at front
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
# deletion of node in side linked list class
    def delete(self,key):
        temp=self.head
        #if key is prsent at head of linked list
        if (temp is not None):
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        # if key in between so search the key to be deleted    
        while (temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        # if key is not in linked list
        if temp ==None:
            return
        prev.next=temp.next
        temp=None
        #print elements
    def printlist(self):
            temp=self.head
            while (temp):
                print(temp.data)
                temp=temp.next
llist = Linkedlist()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printlist()
llist.delete(1)
print ("\nLinked List after Deletion of 1:")
llist.printlist()
 