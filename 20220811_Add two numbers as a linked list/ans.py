# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        inc = 0
        val = l1.val + l2.val + inc
        if val > 9:
            inc = 1
        else:
            inc = 0
        l1 = l1.next
        l2 = l2.next
        l3 = ListNode(val)
        currentnode = l3
        while l1:
            val = l1.val + l2.val + inc
            if val > 9:
                val -= 10
                inc = 1
            else:
                inc = 0
            l1 = l1.next
            l2 = l2.next
            newnode = ListNode(val)
            currentnode.next = newnode
            currentnode = newnode
        return l3
    # Fill this in.


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=' ')
    result = result.next
# 7 0 8
