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
        hashmap = {None : None}  # original node → new node
        curr = head

        # build hashmap by cloning the original list's nodes
        while curr:
            node_clone = Node(curr.val)
            hashmap[curr] = node_clone
            curr = curr.next
        
        # create new copied linked list
        curr = head
        while curr:
            node_clone = hashmap[curr]
            node_clone.next = hashmap[curr.next]
            node_clone.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]
