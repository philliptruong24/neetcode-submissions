# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            tail_node = head.next
            tail2_node = tail_node.next
            head.next = None 

            while tail2_node != None:
                tail_node.next = head
                head = tail_node
                tail_node = tail2_node
                tail2_node = tail2_node.next
            
            tail_node.next = head
            head = tail_node
            return head

                

        