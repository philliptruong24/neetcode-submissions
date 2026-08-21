# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        begin = reverse = prev
        prev = None
        for i in range(1, n):
            prev = reverse
            reverse = reverse.next
        
        if prev:
            prev.next = reverse.next
            
        else:
            begin = reverse.next

        reverse = begin
        prev = None
        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp
        
        return prev

        
        

