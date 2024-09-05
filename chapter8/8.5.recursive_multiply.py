class Solution:
    def recursive_multiply(self, a, b):
        if b > a:
            return self.recursive_multiply(b, a)
        if b == 0:
            return 0

        if b % 2 == 0:
            half_product = self.recursive_multiply(a, b // 2)
            return half_product + half_product
        return a + self.recursive_multiply(a, b - 1)


a = 5
b = 2
solution = Solution()
assert solution.recursive_multiply(a, b) == 10

a = 2
b = 5
solution = Solution()
assert solution.recursive_multiply(a, b) == 10

a = 10
b = 9
solution = Solution()
assert solution.recursive_multiply(a, b) == 90
