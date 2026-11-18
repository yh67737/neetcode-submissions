# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr1,curr2=None,list1,list2
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                temp=curr1.next
                curr1.next=prev
                prev=curr1
                curr1=temp
            else:
                temp=curr2.next
                curr2.next=prev
                prev=curr2
                curr2=temp
        while curr1:
            temp=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=temp
        while curr2:
            temp=curr2.next
            curr2.next=prev
            prev=curr2
            curr2=temp
        curr=prev
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

