class LinkedListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:

    def partition(self, head1, head2):
        head = LinkedListNode()
        dummy = head
        carry = 0
        while head1 and head2:
            total = head1.val + head2.val + carry
            dummy.next = LinkedListNode(total % 10)
            carry = total // 10
            head1 = head1.next
            head2 = head2.next
            dummy = dummy.next

        while head1:
            total = head2.val + carry
            dummy.next = LinkedListNode(total % 10)
            carry = total // 10
            dummy = dummy.next
            head1 = head1.next

        while head2:
            total = head2.val + carry
            dummy.next = LinkedListNode(total % 10)
            carry = total // 10
            dummy = dummy.next
            head2 = head2.next

        return head.next


solution = Solution()

head1 = LinkedListNode(7)
head1.next = LinkedListNode(1)
head1.next.next = LinkedListNode(6)

head2 = LinkedListNode(5)
head2.next = LinkedListNode(9)
head2.next.next = LinkedListNode(2)

answer = solution.partition(head1, head2)
expected = [2, 1, 9]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next

head1 = LinkedListNode(7)

head2 = LinkedListNode(5)
head2.next = LinkedListNode(9)
head2.next.next = LinkedListNode(2)

answer = solution.partition(head1, head2)
expected = [2, 0, 3]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next
