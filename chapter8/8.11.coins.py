class Solution:
    def __init__(self, coin_list):
        self.coin_list = coin_list
        self.answer = 0
        self.paths = set()

    def coins(self, n):

        def backtrack(current_target, path):
            if current_target == 0 and tuple(sorted(path)) not in self.paths:
                self.answer += 1
                self.paths.add(tuple(sorted(path)))

                return
            if current_target < 0:
                return

            for coin in self.coin_list:
                current_target -= coin
                path.append(coin)
                backtrack(current_target, path)
                current_target += coin
                path.pop()

        backtrack(n, [])
        return self.answer


coin_list = [1, 5, 10, 25]
solution = Solution(coin_list)
assert solution.coins(1) == 1
solution = Solution(coin_list)
assert solution.coins(5) == 2
solution = Solution(coin_list)
assert solution.coins(9) == 2
solution = Solution(coin_list)
assert solution.coins(11) == 4
