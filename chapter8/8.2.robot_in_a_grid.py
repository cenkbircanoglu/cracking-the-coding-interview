class Solution:
    def __init__(self):
        self.answer = None

    def dfs(self, grid, x, y, path):
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            path.append((x, y))
            self.answer = path.copy()
        path.append((x, y))
        grid[x][y] = 0
        if x + 1 < len(grid) and grid[x + 1][y] == 1:
            self.dfs(grid, x + 1, y, path)
        if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
            self.dfs(grid, x, y + 1, path)
        path.pop()

    def find_path(self, grid):
        self.dfs(grid, 0, 0, [])
        return self.answer


grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]]

solution = Solution()
path = solution.find_path(grid)
expected = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3)]
assert path == expected
