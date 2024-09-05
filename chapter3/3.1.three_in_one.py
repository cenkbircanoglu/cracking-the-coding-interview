class ThreeStacks:
    def __init__(self, stack_size=100):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * (self.num_stacks * self.stack_size)
        self.tops = [-1] * self.num_stacks

    def push(self, stack_num, value):
        self.tops[stack_num] += 1
        index = stack_num * self.stack_size + self.tops[stack_num]
        self.array[index] = value

    def pop(self, stack_num):
        index = stack_num * self.stack_size + self.tops[stack_num]
        value = self.array[index]
        self.array[index] = None
        self.tops[stack_num] -= 1
        return value

    def peek(self, stack_num):
        index = stack_num * self.stack_size + self.tops[stack_num]
        return self.array[index]

    def is_empty(self, stack_num):
        return self.tops[stack_num] == -1

    def is_full(self, stack_num):
        return self.tops[stack_num] >= self.stack_size - 1

    def size(self, stack_num):
        return self.tops[stack_num] + 1


stacks = ThreeStacks(stack_size=5)

stacks.push(0, 'A1')
stacks.push(0, 'A2')
stacks.push(1, 'B1')
stacks.push(2, 'C1')
stacks.push(1, 'B2')
stacks.push(2, 'C2')
stacks.push(2, 'C3')

popped = stacks.pop(1)
assert popped == "B2"

top = stacks.peek(2)
assert top == "C3"

assert stacks.is_empty(0) == False

assert stacks.size(2) == 3
