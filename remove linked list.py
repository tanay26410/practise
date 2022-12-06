#remove linked list
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val==val:
            head=head.next
        x=head
        y=head
        while x is not None:
            if x.val==val:
                x=x.next
                y.next=x
            else:
                y=x
                x=x.next
        return head