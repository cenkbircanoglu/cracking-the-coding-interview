class Solution:

    def __init__(self):
        self.stack = []

    def push(self, val):
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))
        else:
            self.stack.append((val, val))

    def pop(self):
        return self.stack.pop()[0]

    def min(self):
        return self.stack[-1][0]
