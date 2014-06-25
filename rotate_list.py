# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
      if head == None or k == 0:
        return head
      tail   = head
      length = 1
      while tail.next != None:
        tail = tail.next
        length += 1

      keep = (length - k)%length
      if keep == 0:
        return head

      i = 0
      tail2 = head
      while i < keep:
        prev  = tail2
        tail2 = tail2.next
        i += 1

      new_head = tail2
      prev.next = None
      print prev.val
      print new_head.val
      print tail.val
      tail.next = head

      return new_head

    def printList(self, head):
      while head != None:
        print head.val, "=>",
        head = head.next
      print "None"

    def arr2list(self, arr):
        head = ListNode(0)
        curr = head
        for (i, a) in enumerate(arr):
            curr.next = ListNode(a)
            curr = curr.next
        head = head.next
        return head


# arr = [1,2,3,4,5]
arr = [1,2]
arr = [1]

s = Solution()
head = s.arr2list(arr)
s.printList(head)

khead = s.rotateRight(head, 1)
s.printList(khead)