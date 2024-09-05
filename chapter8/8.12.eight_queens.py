class Solution:
    def eight_queens(self):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(row - i) == abs(col - board[i]):
                    return False
            return True

        def backtrack(board, row):
            if row == len(board):
                self.answer.append(board[:])
                return

            for col in range(len(board)):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)

        self.answer = []
        board = [-1] * 8
        backtrack(board, 0)
        return self.answer

solution = Solution()
answer = solution.eight_queens()
for i in answer:
    print(i)