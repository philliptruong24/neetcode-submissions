# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        dummy = curr = ListNode(0, None)
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

            curr.next = ListNode(currSum, None)
            curr = curr.next
        
        if carryOver:
            curr.next = ListNode(1, None)
        return dummy.next

    
        