class Solution:

    def paint_fill(self, image, start_r, start_c, new_color):
        rows, cols = len(image), len(image[0])
        original_color = image[start_r][start_c]

        if original_color == new_color:
            return image

        def fill(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return

            image[r][c] = new_color

            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        fill(start_r, start_c)
        return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
start_r, start_c = 1, 1
new_color = 2
solution = Solution()
result = solution.paint_fill(image, start_r, start_c, new_color)
for row in result:
    print(row)
