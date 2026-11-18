class node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hashmap={}
        self.left,self.right=node(0,0),node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        
    
    def insert(self,n):
        prev=self.right.prev
        prev.next=n
        n.prev=prev
        self.right.prev=n
        n.next=self.right


    def remove(self,n):
        prev,next=n.prev,n.next
        prev.next=next
        next.prev=prev
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            n=self.hashmap[key]
            self.remove(n)
            self.insert(n)
            return n.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            n=node(key,value)
            self.hashmap[key]=n
            self.insert(n)
            if len(self.hashmap)>self.cap:
                del self.hashmap[self.left.next.key]
                self.remove(self.left.next)
        else:
            n=self.hashmap[key]
            n.val=value
            self.remove(n)
            self.insert(n)
        
