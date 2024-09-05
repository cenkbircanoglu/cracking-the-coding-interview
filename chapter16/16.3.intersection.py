# TODO
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def on_segment(self, p, q, r):
        """Check if point q lies on segment pr"""
        if max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y):
            return True
        return False

    def orientation(self, p, q, r):
        """Find the orientation of the triplet (p, q, r).
        0 -> p, q and r are collinear
        1 -> Clockwise
        2 -> Counterclockwise
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def do_intersect(self, p1, q1, p2, q2):
        """Main function to check whether the line segment 'p1q1'
        and 'p2q2' intersect."""
        # Find the four orientations needed for general and
        # special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if o1 != o2 and o3 != o4:
            return True

        # Special Cases
        # p1, q1, p2 are collinear and p2 lies on segment p1q1
        if o1 == 0 and self.on_segment(p1, p2, q1):
            return True

        # p1, q1, q2 are collinear and q2 lies on segment p1q1
        if o2 == 0 and self.on_segment(p1, q2, q1):
            return True

        # p2, q2, p1 are collinear and p1 lies on segment p2q2
        if o3 == 0 and self.on_segment(p2, p1, q2):
            return True

        # p2, q2, q1 are collinear and q1 lies on segment p2q2
        if o4 == 0 and self.on_segment(p2, q1, q2):
            return True

        # Doesn't fall in any of the above cases
        return False

    def intersection(self, p1, p2, q1, q2):
        if self.do_intersect(p1, q1, p2, q2):
            A1 = q1.y - p1.y
            B1 = p1.x - q1.x
            C1 = A1 * p1.x + B1 * p1.y

            A2 = q2.y - p2.y
            B2 = p2.x - q2.x
            C2 = A2 * p2.x + B2 * p2.y

            determinant = A1 * B2 - A2 * B1

            if determinant == 0:
                # The lines are parallel. This is a special case.
                return None
            else:
                x = (B2 * C1 - B1 * C2) / determinant
                y = (A1 * C2 - A2 * C1) / determinant
                return Point(x, y)
        return None


p1 = Point(0, 0)
p2 = Point(1, 0)
q1 = Point(1, 1)
q2 = Point(0, -1)

expected = [0.5, 0]
solution = Solution()
assert solution.intersection(p1, p2, q1, q2) == expected
