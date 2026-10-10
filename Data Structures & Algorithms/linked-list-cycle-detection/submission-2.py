# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = set()
        current = head

        while current:
            if current in checked:
                return True

            checked.add(current)
            current = current.next
        return False