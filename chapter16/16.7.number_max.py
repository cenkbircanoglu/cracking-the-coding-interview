class Solution:
    def number_max(self, a: int, b: int) -> int:
        original_a = a
        original_b = b
        while a and b:
            a = a >> 1
            b = b >> 1
        while a > 1:
            a = a >> 1
        while b > 1:
            b = b >> 1
        return a * original_a + b * original_b

    def number_max2(self, a: int, b: int) -> int:
        def flip(bit):
            return 1 ^ bit

        def sign(a):
            return flip((a >> 31) & 0x1)
        k = sign(a - b)
        q = flip(k)
        return a * k + b * q


solution = Solution()
assert solution.number_max(3, 5) == 5
assert solution.number_max2(3, 5) == 5
assert solution.number_max(3, 15) == 15
assert solution.number_max2(3, 15) == 15
assert solution.number_max(3, -15) != 3 # first algorithm is not working for negative numbers
assert solution.number_max2(3, -15) == 3
