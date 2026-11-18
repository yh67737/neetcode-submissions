# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        res=0
        while l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            sum=(val1+val2+res)%10
            tmp=ListNode(sum)
            curr.next=tmp
            curr=curr.next
            res=(val1+val2+res)//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if res>0:
            tmp=ListNode(res)
            curr.next=tmp
        return dummy.next


