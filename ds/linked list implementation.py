#linked list implementation
from dataclasses import dataclass


class Node:
    def __init__(self,data):
            self.data=data
            self.next=None
        
class linkedlist:
    def __init__(self):
         self.head=None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insertafter(self,pre,data):
        if self.head==None:
            return 'Empty'
        new=Node(data)
        new.nexr=pre.next
        pre.next=new
    def insetatend(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return 
        tem=self.head
        while tem.next:
            tem=tem.next
        tem.next=new
    def deletebeg(self,k):
        t=self.head
        c=0
        if k==1:
            self.head=t.next
            return self.head
        
        
    def print(self):
        tem=self.head
        while tem:
            print(tem.data,end=' ')
            tem=tem.next

if __name__=='__main__':
    lis=linkedlist()
    lis.push(1)
    lis.print()
    lis.insetatend('a')
    lis.print()
    lis.insertafter(lis.head.next,5)
    lis.print()

