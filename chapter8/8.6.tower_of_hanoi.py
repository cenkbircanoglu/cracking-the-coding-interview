#TODO

class Tower:
    def __init__(self, disks=None):
        if disks is None:
            self.disks = []
        else:
            self.disks = disks

    def add(self, value):
        if len(self.disks) <= 0:
            self.disks.append(value)
            return
        elif value <= self.disks[-1]:
            self.disks.append(value)
            return
        else:
            return

    def move_top_to(self, destination):
        if len(self.disks) <= 0:
            return
        destination.add(self.disks[-1])
        self.disks.pop()

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)


class Solution:
    def tower_of_hanoi(self, n, source, auxiliary, destination):
        if n == 1:
            return

        self.tower_of_hanoi(n - 1, source, destination, auxiliary)

        # Step 3: Move the n-1 disks from auxiliary to destination
        self.tower_of_hanoi(n - 1, auxiliary, source, destination)


n = 3
Solution().tower_of_hanoi(n, 'A', 'B', 'C')
