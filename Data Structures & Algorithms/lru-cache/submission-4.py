class node:
    def __init__(self,key,value):
        self.key,self.value=key,value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left,self.right=node(0,0),node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.hashmap={}

    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node

    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next=next
        next.prev=prev
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            n=self.hashmap[key]
            self.remove(n)
            self.insert(n)
            return n.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            n=self.hashmap[key]
            n.value=value
            self.remove(n)
            self.insert(n)
        else:
            n=node(key,value)
            self.hashmap[key]=n
            self.insert(n)
        while len(self.hashmap)>self.cap:
            n=self.left.next
            self.remove(n)
            del self.hashmap[n.key]


        
