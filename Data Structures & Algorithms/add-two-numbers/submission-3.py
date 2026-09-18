# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        x = []

        y = []

        curr1 = l1

        curr2 = l2

        while curr1:

            x.append(curr1.val)
          
            curr1 = curr1.next
        while curr2:

            y.append(curr2.val)

            curr2 = curr2.next

        
        int_x = int("".join(map(str,reversed(x))))
        int_y = int("".join(map(str,reversed(y))))

        ans = int_x + int_y 

        if ans == 0:

            return ListNode(0)

        dummynode = ListNode()

        head = dummynode

        while ans:

            rem = ans % 10

            node = ListNode(rem)

            head.next = node

            head = node

            ans = ans // 10
        
        return dummynode.next







        