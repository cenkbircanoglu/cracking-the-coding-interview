class LinkedListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:

    def intersection(self, head1, head2):
        node1, node2 = head1, head2
        while node1 != node2:
            if node1.next == None:
                node1 = head2
            else:
                node1 = node1.next
            if node2.next == None:
                node2 = head1
            else:
                node2 = node2.next

        return node1


solution = Solution()

head1 = LinkedListNode(1)
head1.next = LinkedListNode(2)
head1.next.next = LinkedListNode(3)

head2 = LinkedListNode(7)
head2.next = LinkedListNode(1)
head2.next.next = LinkedListNode(1)
head2.next.next.next = head1.next

assert solution.intersection(head1, head2) == head1.next

head1 = LinkedListNode(1)
head1.next = LinkedListNode(2)
head1.next.next = LinkedListNode(3)

head2 = LinkedListNode(7)
head2.next = LinkedListNode(1)
head2.next.next = LinkedListNode(1)
head2.next.next.next = head1.next.next

assert solution.intersection(head1, head2) == head1.next.next

head1 = LinkedListNode(1)
head1.next = LinkedListNode(2)
head1.next.next = LinkedListNode(3)

head2 = LinkedListNode(7)
head2.next = LinkedListNode(1)
head2.next.next = LinkedListNode(1)
head2.next.next.next = head1

assert solution.intersection(head1, head2) == head1

head1 = LinkedListNode(1)
head1.next = LinkedListNode(2)
head1.next.next = LinkedListNode(3)

head2 = LinkedListNode(7)
head2.next = LinkedListNode(1)
head2.next.next = LinkedListNode(1)

assert solution.intersection(head1, head2) == None
