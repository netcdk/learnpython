"""
Student portion of Zombie mini-project
by CDK
Written on CodeSkultpor.org
"""

import random
import math
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        
		poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        
		poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        
		self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        
		return len(self._zombie_list)    
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        
		for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        
		self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        
		return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        
		for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
		# Create temporary location variables
		grid_height = poc_grid.Grid.get_grid_height(self)
        grid_width = poc_grid.Grid.get_grid_width(self)
        visited = poc_grid.Grid(grid_height, grid_width)
        
		#  Create distance field
		distance_field = [[grid_height * grid_width for dummy in range(grid_width)]
                                                    for dummy in range(grid_height)]
        
		# Determine current entities on board
		entities = []
        if entity_type == HUMAN:
            entities = self._human_list
        else:
            entities = self._zombie_list
        
		# Create boundary queue
		boundary = poc_queue.Queue()
		
		# Fill queue based on selected entity, with associated location
        for entity in entities:
            row = entity[0]
            col = entity[1]
            poc_queue.Queue.enqueue(boundary, entity)
            poc_grid.Grid.set_full(visited, row, col)
            distance_field[row][col] = 0
        
		# Compute distance field
		while boundary:
            current_cell = poc_queue.Queue.dequeue(boundary)
            neighboring = poc_grid.Grid.four_neighbors(self, current_cell[0], current_cell[1])
            for neighbor in neighboring:
                row = neighbor[0]
                col = neighbor[1]
                if poc_grid.Grid.is_empty(visited, row, col) and poc_grid.Grid.is_empty(self, row, col):
                    poc_grid.Grid.set_full(visited, row, col)
                    poc_queue.Queue.enqueue(boundary, neighbor) 
                    distance_field[row][col] = distance_field[current_cell[0]][current_cell[1]] + 1
        return distance_field
        
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        
		humans = self.humans()
        new_human_list = []
        
		for dummy in range(self.num_humans()):
            max_distance = float('-inf')
            human = humans.next()
            possible_moves = poc_grid.Grid.eight_neighbors(self, human[0], human[1]) \
                                + [(human[0], human[1])]
            best_moves = []
            for move in possible_moves:
                if poc_grid.Grid.is_empty(self, move[0], move[1]):
                    distance = zombie_distance_field[move[0]][move[1]]
                    if distance > max_distance:
                        max_distance = distance
                        best_moves = [move]
                    elif distance == max_distance:
                        best_moves.append(move)
            new_human_list.append(random.choice(best_moves))
        self._human_list = new_human_list
            
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        zombies = self.zombies()
        new_zombie_list = []
        for dummy in range(self.num_zombies()):
            min_distance = float('inf')
            zombie = zombies.next()
            possible_moves = poc_grid.Grid.four_neighbors(self, zombie[0], zombie[1]) \
                                + [(zombie[0], zombie[1])]
            best_moves = []
            for move in possible_moves:
                if poc_grid.Grid.is_empty(self, move[0], move[1]):
                    distance = human_distance_field[move[0]][move[1]]
                    if distance < min_distance:
                        min_distance = distance
                        best_moves = [move]
                    elif distance == min_distance:
                        best_moves.append(move)
            new_zombie_list.append(random.choice(best_moves))
        self._zombie_list = new_zombie_list
            
 

# poc_zombie_gui.run_gui(Apocalypse(30, 40))