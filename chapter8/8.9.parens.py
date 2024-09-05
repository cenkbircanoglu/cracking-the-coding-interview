class Solution:
    def __init__(self):
        self.answer = []

    def parens(self, n):
        def backtrack(path, opening_count, closing_count):
            if len(path) == 2 * n:
                self.answer.append(path)
                return

            if opening_count < n:
                backtrack(path + '(', opening_count + 1, closing_count)
            if closing_count < opening_count:
                backtrack(path + ')', opening_count, closing_count + 1)

        backtrack('', 0, 0)
        return self.answer


solution = Solution()
answer = solution.parens(3)
expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
assert sorted(answer) == sorted(expected)
