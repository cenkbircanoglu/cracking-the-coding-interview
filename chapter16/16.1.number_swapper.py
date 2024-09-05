class Solution:
    def swapNumbers(self, numbers, x, y):
        numbers[x] ^= numbers[y]
        numbers[y] ^= numbers[x]
        numbers[x] ^= numbers[y]
        return numbers


numbers = [1, 2]
solution = Solution()
assert solution.swapNumbers(numbers, 0, 1) == [2, 1]

numbers = [1, 2, 3, 4, 5, 6]
solution = Solution()
assert solution.swapNumbers(numbers, 2, 4) == [1, 2, 5, 4, 3, 6]
