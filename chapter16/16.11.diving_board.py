class Solution:
    def diving_board(self, shorter, longer, k):
        if shorter == longer:
            return [shorter * k]
        lengths = []
        for i in range(k + 1):
            length = shorter * (k - i) + longer * i
            lengths.append(length)
        return lengths


solution = Solution()
assert solution.diving_board(1, 2, 3) == [3, 4, 5, 6]
assert solution.diving_board(1, 5, 3) == [3, 7, 11, 15]
