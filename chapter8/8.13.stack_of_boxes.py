class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __lt__(self, other):
        return self.width < other.width and self.depth < other.depth


def max_stack_height(boxes):
    all_rotations = []
    for box in boxes:
        h, w, d = box.height, box.width, box.depth
        all_rotations.append(Box(h, max(w, d), min(w, d)))
        all_rotations.append(Box(w, max(h, d), min(h, d)))
        all_rotations.append(Box(d, max(h, w), min(h, w)))

    all_rotations.sort(key=lambda box: box.width * box.depth, reverse=True)

    n = len(all_rotations)
    dp = [0] * n

    for i in range(n):
        dp[i] = all_rotations[i].height

    for i in range(1, n):
        for j in range(0, i):
            if all_rotations[i].width < all_rotations[j].width and all_rotations[i].depth < all_rotations[j].depth:
                dp[i] = max(dp[i], dp[j] + all_rotations[i].height)

    return max(dp)


# Example usage
boxes = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
print("The maximum height of the stack is:", max_stack_height(boxes))
