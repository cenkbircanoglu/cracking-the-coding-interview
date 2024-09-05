class Solution:
    def factorial_zeros(self, n: int) -> int:
        count = 0
        i = 5
        while n > 0:
            count += n // i
            n //= 5
        return count


N = 5
solution = Solution()
expected = 1
assert solution.factorial_zeros(N) == expected
N = 15
expected = 3
assert solution.factorial_zeros(N) == expected
