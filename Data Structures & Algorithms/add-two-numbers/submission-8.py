# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carryOver = 0
        while l1 or l2:
            currSum = carryOver
            if l1:
                currSum += l1.val
                l1 = l1.next
            if l2:
                currSum += l2.val
                l2 = l2.next
            
            carryOver = currSum // 10
            currSum %= 10

            node.next = ListNode(currSum, None)
            node = node.next
        
        if carryOver:
            node.next = ListNode(carryOver, None)
        
        return dummy.next
        