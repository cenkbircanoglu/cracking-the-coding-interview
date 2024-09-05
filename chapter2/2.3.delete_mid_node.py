class LinkedListNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None

class Solution:

    def delete_mid(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next

        return head




solution = Solution()

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(6)

answer = solution.delete_mid(head)
expected = [1, 2, 4, 5, 6]
i = 0
while answer:
    answer.val = expected[i]
    i += 1
    answer = answer.next


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)

answer = solution.delete_mid(head)
expected = [1, 2, 4, 5]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next



head = LinkedListNode(1)

answer = solution.delete_mid(head)
expected = [1, 2, 4, 5, 6]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next


head = LinkedListNode(1)
head.next = LinkedListNode(2)

answer = solution.delete_mid(head)
expected = [1, 2, 4, 5, 6]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next
