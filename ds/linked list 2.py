
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def print(self):
        if self.head is None:
            print('Linkefd list is empty')
            return 
        temp=self.head
        list=''
        while (temp):
            list+=str(temp.data)+'-->' if temp.next else str(temp.data)
            temp=temp.next
        print(list)
    def length(self):
        if self.head is None:
            print('linked list is empty')
            return
        k=0
        temp=self.head
        while temp:
            k+=1
            temp=temp.next
        return k
    def atbeg(self,data):
        new=Node(data,self.head)
        self.head=new 
    def end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)
    
    def atpos(self,data,loc):
        if loc<0 or loc>self.length():
            print('invalid index')
            return
        if loc==0:
            self.atbeg(data)
        count=0
        temp=self.head
        while temp:
            if loc-1==count:
                new=Node(data,temp.next)
                temp.next=new
                break
            temp=temp.next
            count+=1
    def delete(self,loc):
        if loc<0 or loc>self.length():
            print('invalid length')
            return
        count=0
        temp=self.head
        while temp:
            if loc-1==count:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1
    def values(self,datalist):
        self.head=None
        for data in datalist:
            self.end(data)

ll=Linkedlist()

ll.atbeg(5)
ll.atbeg(6)
ll.atbeg(7)
ll.end(456)

ll.print()
ll.values([4,6,7,8,92,90])
ll.delete(3)
ll.print()



# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)


# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at(1,"blueberry")
#     ll.remove_at(2)
#     ll.print()

#     ll.insert_values([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()
