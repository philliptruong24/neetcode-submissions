# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        prev = None
        curr = head
        for i in range(math.ceil(length / 2)):
            prev = curr
            curr = curr.next
         
        prev.next = None

        reverse = None
        while curr:
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp

        curr = head
        while reverse:
            temp = curr.next
            curr.next = reverse
            reverse = reverse.next
            
            curr = curr.next
            curr.next = temp
            curr = curr.next



