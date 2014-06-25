class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def reverseListRecursive(self, head):
    if head == None:
      return None
    if head.next == None:
      return head
    second = head.next
    head.next = None
    reverseRest = self.reverseListRecursive(second)
    second.next = head
    return reverseRest

  def reverseListIterative(self, head):
    curr = head.next
    head.next = None
    prev = head
    while curr != None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev

  def arr2list(self, arr):
    head = ListNode(0)
    curr = head
    for (i, a) in enumerate(arr):
        curr.next = ListNode(a)
        curr = curr.next
    head = head.next
    return head

  def list2arr(self, head):
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    return arr

  def to_array(self):
    return self.list2arr(self)

# ln = ListNode(0)
# arr = [3, 5, 6]
# head = ln.arr2list(arr)
# # reveresed = ln.reverseListRecursive(head)
# reveresed = ln.reverseListIterative(head)
# print ln.list2arr(reveresed)
