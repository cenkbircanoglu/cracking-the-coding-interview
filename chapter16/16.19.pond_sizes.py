class Solution:
    def pond_sizes(self, land):
        def dfs(i, j):
            res = 1
            land[i][j] = 1
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if land[x][y] == 0 <= x < m > y >= 0:
                        res += dfs(x, y)
            return res

        m, n = len(land), len(land[0])
        return sorted(dfs(i, j) for i in range(m) for j in range(n) if land[i][j] == 0)


solution = Solution()
land = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]
assert solution.pond_sizes(land) == [1, 2, 4]
