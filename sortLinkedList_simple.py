# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        # QuickSort, does not swap pivots, stack overflow easily
        len = 0
        tail = head
        while tail != None:
            len += 1
            tail = tail.next
        pivot = head
        return self.partition(head, len)

    def partition(self, head, len):
        if len<2:
            return head

        pivot = head
        tail  = head
        head  = ListNode(0)
        left  = head
        l = 0
        l_len = 0
        r_len = len-1

        while tail.next != None and l<len-1:
            if tail.next.val < pivot.val:
                left.next = tail.next
                left = left.next
                tail.next = tail.next.next
                r_len -= 1
                l_len += 1
                left.next = pivot
            elif tail.next.val >= pivot.val:
                tail = tail.next
            l += 1
        left.next = pivot

        head_l = self.partition(head.next,  l_len)
        head_r = self.partition(pivot.next, r_len)
        head.next  = head_l
        pivot.next = head_r

        return head.next