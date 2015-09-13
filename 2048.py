"""
Clone of 2048 game by CDK
Written on CodeSkulptor.org
"""

import poc_2048_gui, random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    # Create working lists
    merged = []
    final = []

    # Shift all non-zero variables to the beginning of the list
    for cell in line:
        if cell != 0:
            merged.append(cell)
   
    # Start merging!
    for target in (range(len(merged)-1)):
        if merged[target] == merged[target + 1]:
            merged[target] = merged[target] + merged[target + 1]
            merged[target + 1] = 0
    
    # Shift non-zeroes again, and compare original line length to
    # the current list length, then add zeroes at end to refill to
    # to origial length
    for cell in merged:
        if cell != 0:
            final.append(cell)
    
    if len(final) < len(line):
        more_zeroes = [0] * (len(line) - len(final)) 
        final.extend(more_zeroes)
    
    # Push the output
    return final

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # Take the height and width of the grid
        # and creates the initial 2048 board.
        self._height = grid_height
        self._width = grid_width
        self.reset()
        
        # Create a dictionary of indices for initial tiles in each direction
        self._d_indxs = {UP: [(0, i) for i in range(self._width)],
                         DOWN: [((self._height - 1), i) for i in range(self._width)],
                         LEFT: [(i, 0) for i in range(self._height)],
                         RIGHT: [(i, (self._width - 1)) for i in range(self._height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Calculate number of steps based on direction
        if (direction == UP) or (direction == DOWN):
            steps = range(self._height)
        else:
            steps = range(self._width)
        
        # Create flag for change
        change = False
        
        # Step (using our caluclated 'steps' value) through
        # each column or row (depending on direction)
        for initial_tile in self._d_indxs[direction]:
            merging = []
            for step in steps:
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                merging.append(self._grid[row][col])
            merged = merge(merging)
            for step in steps:
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                self._grid[row][col] = merged[step]
            if merged != merging:
                change = True
        
        # Add new tile if board has changed
        if change == True:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zeroes_indices = [] 
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    zeroes_indices.append([row, col])
        target_index = random.choice(zeroes_indices)
        self._grid[target_index[0]][target_index[1]] = random.choice(([2]*9 + [4]))
                    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(6, 4))
