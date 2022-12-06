#flatten multilevel doubly linked list
def flatten(head):
        res = head
    
        def flat(nde):
            cur= nde
            while nde:
                if nde.child is not None:
                    call = flat(nde.child)
                    call.next = nde.next
                    if nde.next:
                        nde.next.prev = call
                    nde.next = nde.child
                    nde.child.prev = nde
                    cur= call
                    nde.child = None
                    nde = call.next
                else:
                    cur= nde
                    nde = nde.next
            return cur
        
        flat(head)
        return res