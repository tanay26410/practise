#merge sorted linked list
def mergeLists(headA, headB):
    if(headA is None):
                return headB
    elif(headB is None):
                return headA

    if(headA.data <= headB.data):
                result = headA
                result.next = mergeLists(headA.next, headB)
    else:
                result = headB
                result.next = mergeLists(headA, headB.next)
                
    return result

def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data<head2.data:
        s=head1
        s.next=mergeLists(head1.next,head2)
        
    else:
        s=head2
        s.next=mergeLists(head1,head2.next)
    return s