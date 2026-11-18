# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        curr1,curr2=list1,list2
        while curr1 and curr2:
            if curr1.val <=curr2.val:
                temp=curr1.next
                tail.next=curr1
                curr1=temp
            else:
                temp=curr2.next
                tail.next=curr2
                curr2=temp
            tail=tail.next
        if curr1:
            tail.next=curr1
        if curr2:
            tail.next=curr2
        return dummy.next
       

