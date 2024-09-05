class Results:
    X = "X"
    O = "O"
    D = "Draw"
    P = "Pending"


class Solution:
    def tic_tac_win(self, board):
        N = len(board)
        row_counter = [0] * N
        column_counter = [0] * N
        diagonal_counter = 0
        anti_diagonal_counter = 0
        empty_cell_found = False
        for r in range(N):
            for c in range(N):
                val = None
                if board[r][c] is None:
                    empty_cell_found = True
                    continue
                if board[r][c] == Results.X:
                    val = 1
                if board[r][c] == Results.O:
                    val = -1
                if val:
                    row_counter[r] += val
                    column_counter[c] += val
                    if r + c == N - 1:
                        anti_diagonal_counter += val
                    if r == c:
                        diagonal_counter += val
                    if abs(row_counter[r]) == N or abs(column_counter[c]) == N or abs(diagonal_counter) == N or abs(
                            anti_diagonal_counter) == N:
                        return Results.X if val == 1 else Results.O
        return Results.P if empty_cell_found else Results.D


solution = Solution()

board = [["O", None, "X"],
         [None, "X", "O"],
         ["X", None, "O"]
         ]
expected = "X"
assert solution.tic_tac_win(board) == expected
board = [["O", None, "X"],
         [None, "O", "O"],
         ["X", None, "O"]
         ]
expected = "O"
assert solution.tic_tac_win(board) == expected
board = [["O", "0", "X"],
         ["X", "X", "O"],
         ["O", "X", "O"]
         ]
expected = "Draw"
assert solution.tic_tac_win(board) == expected
board = [["O", "0", "X"],
         ["X", "X", "O"],
         ["O", "X", None]
         ]
expected = "Pending"
assert solution.tic_tac_win(board) == expected
