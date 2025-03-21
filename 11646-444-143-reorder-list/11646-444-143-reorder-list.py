# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge case: If the list is empty or contains only one element, return early
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list starting from the slow pointer
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Merge the two halves of the list
        first, second = head, prev  # first is the start of the first half, second is the reversed second half
        while second:  # Merge until the second half ends
            # Save the next nodes
            temp1, temp2 = first.next, second.next
            
            # Reorder the nodes
            first.next = second
            if temp1 is None:  # If first half ends, no need to link to temp1
                break
            second.next = temp1
            
            # Move the pointers forward
            first = temp1
            second = temp2
        
        # The last node of the first half points to None to complete the list
        if first:
            first.next = None
