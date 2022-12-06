#lenght of ln is odd or even

def isLengthEvenOrOdd(head):
    # Code here
    k=0
    while head:
        k+=1
        head=head.next
        
    if k%2==0:
        return 0
    else:
        return 1