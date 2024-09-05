# Directions: N, E, S, W (clockwise rotation)
DIRECTIONS = ['N', 'E', 'S', 'W']

# Movement vectors for the directions
MOVES = {
    'N': (-1, 0),  # Move up
    'E': (0, 1),  # Move right
    'S': (1, 0),  # Move down
    'W': (0, -1)  # Move left
}


class LangtonsAnt:
    def __init__(self, grid_size):
        self.grid = {}  # Using a dictionary to store the grid, only modified cells are stored
        self.ant_x = grid_size // 2  # Starting position at the center of the grid
        self.ant_y = grid_size // 2
        self.direction = 'N'  # Ant starts facing North

    def get_color(self, x, y):
        """Return the color of the cell: 0 for white, 1 for black."""
        return self.grid.get((x, y), 0)

    def flip_color(self, x, y):
        """Flip the color of the cell."""
        self.grid[(x, y)] = 1 - self.get_color(x, y)

    def turn_right(self):
        """Turn 90 degrees to the right."""
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index + 1) % 4]

    def turn_left(self):
        """Turn 90 degrees to the left."""
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index - 1) % 4]

    def move_forward(self):
        """Move the ant forward in the current direction."""
        move_x, move_y = MOVES[self.direction]
        self.ant_x += move_x
        self.ant_y += move_y
        print(self.ant_x, self.ant_y)

    def step(self):
        """Simulate one step of Langton's Ant."""
        # Get the current color of the cell
        current_color = self.get_color(self.ant_x, self.ant_y)

        # Turn and flip the color
        if current_color == 0:
            self.turn_right()  # White: Turn right
        else:
            self.turn_left()  # Black: Turn left

        # Flip the color of the current cell
        self.flip_color(self.ant_x, self.ant_y)

        # Move the ant forward in the new direction
        self.move_forward()

    def simulate(self, steps):
        """Simulate the ant for a given number of steps."""
        for _ in range(steps):
            self.step()

        return self.grid  # Return the grid for visualization or analysis


# Example usage:
ant = LangtonsAnt(grid_size=101)  # Create an ant on a 101x101 grid
ant.simulate(11000)  # Simulate 11,000 steps

# The grid now contains the state of each modified cell
