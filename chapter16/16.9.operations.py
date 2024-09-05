class Solution:
    def multiply(self, a, b):
        if a < b:
            return self.multiply(b, a)
        if b == 0:
            return 0
        return a + self.multiply(a, b - 1)

    def divide(self, a, b):
        if b == 0:
            return -1
        if a < b:
            return 0
        return 1 + self.divide(a - b, b)

    def subtract(self, a, b):
        return a + ~b + 1


solution = Solution()

assert solution.multiply(3, 5) == 15
assert solution.multiply(5, 3) == 15
assert solution.divide(15, 3) == 5
assert solution.divide(15, 5) == 3
assert solution.divide(15, 4) == 3
assert solution.divide(15, 0) == -1
assert solution.subtract(15, 3) == 12
assert solution.subtract(15, 5) == 10
