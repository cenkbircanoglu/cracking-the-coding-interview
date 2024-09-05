from collections import defaultdict
from math import gcd


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def best_line(self, points):
        def slope(p1, p2):
            """Calculate the slope between two points p1 and p2."""
            dx = p2.x - p1.x
            dy = p2.y - p1.y

            # Handle the vertical line case (infinite slope)
            if dx == 0:
                return (float('inf'), 0)  # Represent a vertical line with infinity

            # Reduce the slope using GCD to avoid floating-point precision issues
            g = gcd(dy, dx)
            slope_y = dy // g
            slope_x = dx // g

            # Return the normalized slope (dy/dx)
            return (slope_y, slope_x)

        n = len(points)
        if n < 2:
            return n

        max_points = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            cur_max = 0

            for j in range(i + 1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    # If the points are the same, treat as duplicate
                    duplicate += 1
                else:
                    s = slope(points[i], points[j])
                    slopes[s] += 1
                    cur_max = max(cur_max, slopes[s])

            # Total points on the line: cur_max + duplicates
            max_points = max(max_points, cur_max + duplicate)

        return max_points


solution = Solution()

points = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 1), Point(2, 1)]
assert solution.best_line(points) == 3
