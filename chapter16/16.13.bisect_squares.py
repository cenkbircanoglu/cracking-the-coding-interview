class Square:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Solution:
    def bisect_squares(self, square1, square2):
        if square1.x1 > square2.x1:
            return self.bisect_squares(square2, square1)
        if square1.x2 < square2.x1 or square1.y2 < square2.y1:
            return None
        if square1.x2 == square2.x1 or square1.y2 == square2.y1:
            return square1.x2, square1.y2
        if square1.x2 < square2.x2:
            return square1.x2, square1.y2
        return square2.x1, square2.x1


solution = Solution()

assert solution.bisect_squares(Square(0, 0, 2, 2), Square(1, 1, 3, 3)) == (2, 2)
assert solution.bisect_squares(Square(0, 0, 2, 2), Square(2, 2, 4, 4)) == (2, 2)
assert solution.bisect_squares(Square(0, 0, 2, 2), Square(3, 3, 4, 4)) == None
assert solution.bisect_squares(Square(0, 0, 2, 2), Square(3, 3, 5, 5)) == None
