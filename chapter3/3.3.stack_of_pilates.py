class LinkedNode:
    def __init__(self, value=None, next_node=None) -> None:
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def push(self, value):
        node = LinkedNode(value, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        temp_value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return temp_value


class SetOfStacks:
    def __init__(self, max_height):
        self.max_height = max_height
        self.stacks = [Stack()]
        self.i = 0

    def push(self, value):
        if self.stacks[self.i].size >= self.max_height:
            self.stacks.append(Stack())
            self.i += 1
        self.stacks[self.i].push(value)

    def pop(self):
        if self.stacks[self.i].is_empty():
            if self.i == 0:
                return None
            self.stacks.pop(self.i)
            self.i -= 1
        return self.stacks[self.i].pop()

    def pop_at(self, index):
        if self.stacks[index].is_empty():
            if index <= 0:
                return None
            self.stacks.pop(index)
            self.i -= 1
            index -= 1
        return self.stacks[index].pop()
