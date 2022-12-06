class dll():
    def __init__(self):
        self.k= 0
        self.val = 0
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.size = 0
        self.cap = capacity
        self.h, self.t = dll(), dll()
        
        self.h.next = self.t
        self.t.prev = self.h

    def get(self, key: int) -> int:
        node = self.d.get(key, None)
        if not node:
            return -1
        
        self.removenode(node)
        self.addnode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.d.get(key, None)
        if not node:
            newNode = dll()
            newNode.k= key
            newNode.val = value
            self.d[key] = newNode
            self.addnode(newNode)
            self.size += 1
            if self.size > self.cap:
                t = self._pop_t()
                del self.d[t.key]
                self.size -= 1
        else:
            node.val= value
            self.removenode(node)
            self.addnode(node)
        
    def removenode(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev

    def addnode(self, node):
        node.prev = self.h
        node.next = self.h.next
        
        self.h.next.prev = node
        self.h.next = node
    
    def _pop_t(self):
        res = self.t.prev
        self.removenode(res)
        return res