class Solution:
    def triple_step(self, n):
        if n < 0:
            return 0

        T0 = 1
        if n >= 1:
            T1 = 1
            T2 = T1
            T3 = T1
        if n >= 2:
            T2 = T1 + T0
            T3 = T2
        if n > 2:
            for _ in range(3, n + 1):
                T3 = T2 + T1 + T0
                T0 = T1
                T1 = T2
                T2 = T3

        return T3


solution = Solution()
n = 1
assert solution.triple_step(n) == 1
n = 2
assert solution.triple_step(n) == 2
n = 3
assert solution.triple_step(n) == 4
n = 4
assert solution.triple_step(n) == 7
n = 5
assert solution.triple_step(n) == 13
