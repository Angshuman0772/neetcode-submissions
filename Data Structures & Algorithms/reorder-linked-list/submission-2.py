# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        # find middle | slow is the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # we need to reverse the entire list from the middle
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge them alternatively
        first = head
        second = prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2