#lfu cache
class Node:
    def __init__(self,key=0,value=0,freq=1):
        self.val=value
        self.k=key
        self.freq=freq
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next,self.tail.prev=self.tail,self.head
        self.len=0
    def removenode(self,node):
        prv,new=node.prev,node.next
        prv.next=new
        new.prev=prv
    def addnode(self,node):
        prv,new=self.tail.prev,self.tail
        prv.next=new.prev=node
        node.next,node.prev=new,prv
        
class LFUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.fl={} #freq :dllist
        self.d={}    #key:node
    def get(self, key: int) -> int:
        if key in self.d:
            node=self.d[key]
            freq=node.freq
            cur=freq+1
            #removefrom prev list
            self.fl[freq].removenode(node)
            self.fl[freq].len-=1
            #add to new list
            node.freq=cur
            #buld cur list
            if cur not in self.fl:
                self.fl[cur]=dll()
            self.fl[cur].addnode(node)
            self.fl[cur].len+=1
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        cur=1
        if key in self.d:
            node=self.d[key]
            freq=node.freq
            cur=freq+1
            self.fl[freq].removenode(node)
            self.fl[freq].len-=1
        elif len(self.d)==self.cap:
            for i in range(1,len(self.fl)+1):
                #delete lfu node
                if self.fl[i].len>0:
                    lfu=self.fl[i].head.next
                    self.fl[i].removenode(lfu)
                    self.fl[i].len-=1
                    del self.d[lfu.k]
                    break
        node=Node(key,value,cur)
        #build cur list
        
        if cur not in self.fl:
            self.fl[cur]=dll()
        self.fl[cur].addnode(node)
        self.fl[cur].len+=1
        self.d[key]=node