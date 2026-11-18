"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        dummy=Node(0)
        prev=dummy
        hashtable=dict()
        while curr:
            tmp=Node(curr.val)
            prev.next=tmp
            prev=prev.next
            hashtable[curr]=tmp
            curr=curr.next
        curr=head
        prev=dummy.next
        while curr:
            prev.random=hashtable.get(curr.random,None)
            prev=prev.next
            curr=curr.next
        return dummy.next

