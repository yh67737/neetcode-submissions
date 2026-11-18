# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        slow,fast=dummy,head
        count=0
        while fast:
            fast=fast.next
            count+=1
        count=count-n
        cnt=0
        while cnt!=count:
            slow=slow.next
            cnt+=1
        slow.next=slow.next.next
        return dummy.next
        
        