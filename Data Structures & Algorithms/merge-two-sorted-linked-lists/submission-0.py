# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a placeholder node that will sit before the merged list
        # tail points to the last node in the merged list (initially the dummy)
        # We will keep attaching nodes to tail.next and move tail forward
        dummy = ListNode()
        tail = dummy

        # Continue while BOTH lists still have nodes 
        # Compare values of current nodes in each list 
        # And attach to merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If list1 / list2 still has nodes left, attach the rest
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next