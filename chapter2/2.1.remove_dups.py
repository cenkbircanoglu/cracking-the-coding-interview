class LinkedListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:

    def remove_dups(self, head):
        hash_table = {head.val: True}
        while head is not None:
            if head.next is not None:
                if hash_table.get(head.next.val, None) is not None:
                    head.next = head.next.next
                else:
                    hash_table[head.next.val] = True
            head = head.next
        return head


solution = Solution()

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(6)

answer = solution.remove_dups(head)
expected = [1, 2, 3, 4, 5, 6]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(5)

answer = solution.remove_dups(head)
expected = [1, 2, 3, 4, 5]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(1)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(5)

answer = solution.remove_dups(head)
expected = [1, 2, 4, 5]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next
