#gfg addone
def addOne(self,head):
        #Returns new head of linked List.
        temp=head
        num=''
        while temp:
            num=num+str(temp.data)
            temp=temp.next
        res=int(num)+1
        l=LinkedList()
        for i in str(res):
            l.insert(i)
        return l.head