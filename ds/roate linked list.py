#roate linked list
from socket import J1939_IDLE_ADDR


def rotate(head,k):
    if k==0:
        return 
    cur=head
    while cur.next:
        cur=cur.next
    cur.next=head
    cur=head
    for i in range(k-1):
        cur=cur.next
    head=cur.next
    cur.next=None
    return head