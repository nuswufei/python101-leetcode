# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        cur = dummyNode
        carry = 0
        while carry != 0 or l1 != None or l2 != None:
            val1 = 0 if l1 == None else l1.val
            val2 = 0 if l2 == None else l2.val
            sum = val1 + val2 + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1 if l1 == None else l1.next
            l2 = l2 if l2 == None else l2.next
        return dummyNode.next
