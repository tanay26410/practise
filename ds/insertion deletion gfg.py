#insertion deletion gfg
def insertAtBegining(self,head,x):
        # code here 
        new=Node(x)
        if head:
            new.next=head

        head=new
        return head
    #Function to insert a node at the end of the linked list.
def insertAtEnd(self,head,x):
        # code here 
        temp=head
        new=Node(x)
        if head==None:
            head=new
        else:
            while (temp.next):
                temp=temp.next
            temp.next=Node(x)
        return head