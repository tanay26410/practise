#delete linked list
def delNode(head, k):
    # Code here
    temp=head
    count=0
    if k==1:
        head=temp.next
        return head
    while temp:
        if k-1==count:
            break
        prev=temp
        temp=temp.next
        count+=1
    if temp==None:
        return 
    prev.next=temp.next
    return head