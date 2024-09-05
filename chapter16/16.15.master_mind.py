from collections import Counter


class Solution:
    def master_mind(self, solution, guess):
        x = sum(a == b for a, b in zip(solution, guess))
        y = sum((Counter(solution) & Counter(guess)).values())
        return [x, y - x]


solution = Solution()
assert solution.master_mind("RGBY", "GGRR") == [1, 1]
