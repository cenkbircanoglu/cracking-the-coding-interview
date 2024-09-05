class Solution:
    def sorted_matrix_search(self, matrix, target):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return row, col
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return None


# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
assert solution.sorted_matrix_search(matrix, 5) == (1, 1)
