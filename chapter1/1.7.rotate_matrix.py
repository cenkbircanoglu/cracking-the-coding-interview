class Solution:
    def transpose(self, matrix):
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
        return matrix

    def reverse(self, matrix):
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]
        return matrix

    def rotate_matrix(self, matrix):
        return self.reverse(self.transpose(matrix))


"""
1   2   3
4   5   6
7   8   9

7   4   1
8   5   2
9   6   3

1   4   7
2   5   8
3   6   9
 Transpose + Reverse rows
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

solution = Solution()
answer = solution.rotate_matrix(matrix)
for r1, r2 in zip(answer, expected):
    for c1, c2 in zip(r1, r2):
        assert c1 == c2
