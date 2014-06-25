import listnode
class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    result = listnode.ListNode(0)
    rl1 = result.reverseListRecursive(l1)
    rl2 = result.reverseListRecursive(l2)

    curr   = result
    carry  = 0
    while rl1 and rl2:
      sum = rl1.val + rl2.val + carry
      carry = 0
      if sum > 9:
        carry = 1
        sum = sum - 10
      curr.next = listnode.ListNode(sum)
      curr = curr.next
      rl1 = rl1.next
      rl2 = rl2.next

    if rl1:
      rest = rl1
    else:
      rest = rl2

    if carry:
      curr.next = listnode.ListNode(1)

    while rest:
      sum = rest.val + carry
      carry = 0
      if sum > 9:
        carry = 1
        sum = sum - 10
      curr.next = listnode.ListNode(sum)
      curr = curr.next
      rest = rest.next

    if carry:
      curr.next = listnode.ListNode(1)

    result = result.reverseListRecursive(result.next)
    return result

ln = listnode.ListNode(0)
arr1 = [7,0,3,6,7,3,2,1,5]
arr2 = [9,2,5,5,6,1,2,2,4]
l1 = ln.arr2list(arr1)
l2 = ln.arr2list(arr2)

s = Solution()
result = s.addTwoNumbers(l1,l2)
print ln.list2arr(result)