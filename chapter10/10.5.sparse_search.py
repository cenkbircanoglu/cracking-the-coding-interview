class Solution:
    def sparse_search(self, arr, target):
        def binary_search(arr, left, right, target):
            if left > right:
                return -1

            mid = (left + right) // 2

            # If mid is an empty string, find the closest non-empty string
            if arr[mid] == "":
                # Initialize mid_left and mid_right to search both sides
                mid_left, mid_right = mid - 1, mid + 1

                # Find the closest non-empty string
                while True:
                    if mid_left < left and mid_right > right:
                        return -1  # No non-empty string found
                    elif mid_right <= right and arr[mid_right] != "":
                        mid = mid_right
                        break
                    elif mid_left >= left and arr[mid_left] != "":
                        mid = mid_left
                        break
                    mid_right += 1
                    mid_left -= 1

            # Perform the standard binary search comparison
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return binary_search(arr, mid + 1, right, target)
            else:
                return binary_search(arr, left, mid - 1, target)

        return binary_search(arr, 0, len(arr) - 1, target)


arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = "ball"

solution = Solution()
assert solution.sparse_search(arr, target) == 4
