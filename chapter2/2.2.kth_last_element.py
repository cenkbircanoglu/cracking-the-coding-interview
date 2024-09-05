class LinkedListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:

    def kth_last_element(self, head, k):
        pointer1 = head
        pointer2 = head
        while k > 0:
            pointer1 = pointer1.next
            k -= 1

        while pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer2.val


solution = Solution()

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(6)

assert solution.kth_last_element(head, 3) == 4

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(5)

assert solution.kth_last_element(head, 5) == 2

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(1)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(5)

assert solution.kth_last_element(head, 2) == 5
