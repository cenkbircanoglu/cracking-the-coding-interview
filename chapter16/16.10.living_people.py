class Solution:
    def living_people(self, people, min_year, max_year):
        years = [0] * (max_year - min_year + 2)
        for person in people:
            years[person[0] - min_year] += 1
            years[person[1] - min_year + 1] -= 1
        max_alive = 0
        max_alive_year = 0
        current_alive = 0
        for i in range(len(years)):
            current_alive += years[i]
            if current_alive > max_alive:
                max_alive = current_alive
                max_alive_year = i
        return max_alive_year + min_year


solution = Solution()
assert solution.living_people([(1900, 1950), (1940, 2000), (1920, 1980)], 1900, 2000) == 1940
