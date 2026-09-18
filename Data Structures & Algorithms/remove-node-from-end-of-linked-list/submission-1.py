# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        curr = head

        length = 0

        while curr:

            length += 1

            curr = curr.next
        
        delnode = length - n

        if delnode == 0:

            return head.next

        cnt = 0

        tmp = head

        while (cnt != delnode - 1):

            tmp = tmp.next
            cnt += 1
        
        tmp.next = tmp.next.next

        return head





