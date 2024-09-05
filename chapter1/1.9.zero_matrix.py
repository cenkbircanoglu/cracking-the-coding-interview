class Solution:

    def zero_matrix(self, matrix):
        zero_columns = []
        zero_rows = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zero_columns.append(c)
                    zero_rows.append(r)
        for r in zero_rows:
            matrix[r] = [0] * len(matrix[r])

        for r in range(len(matrix)):
            for c in zero_columns:
                matrix[r][c] = 0

        return matrix


"""
1   2   0   3
0   5   6   7   
7   8   9   10

0   0   0   0
0   0   0   0   
0   8   0   10

 Transpose + Reverse rows
"""

matrix = [[1, 2, 0, 3],
          [0, 5, 6, 7],
          [7, 8, 9, 10]]
expected = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 8, 0, 10]]

solution = Solution()
answer = solution.zero_matrix(matrix)
for r1, r2 in zip(answer, expected):
    for c1, c2 in zip(r1, r2):
        assert c1 == c2
