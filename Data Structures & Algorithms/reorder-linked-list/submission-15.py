# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse = slow.next
        slow.next = None

        prev = None
        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp
        
        reverse = prev
        forward = head

        while reverse:
            temp1 = forward.next
            temp2 = reverse.next

            forward.next = reverse
            reverse.next = temp1

            forward = temp1
            reverse = temp2
        


