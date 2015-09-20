"""
Monte Carlo Tic-Tac-Toe Player by CDK
Written on CodeSkulptor.org
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 50       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player 
    by making random moves, alternating between players. The 
    function should return when the game is over. The modified board
    will contain the state of the game, so the function does not 
    return anything. In other words, the function should modify the 
    board input.
     """
    
    # Create temporary player and board objects for simulation
    sim_player = player
    
    # Run simulation and return completed board
    for dummy in range(len(board.get_empty_squares())):

        # Select an empty square at random, and move to it
        choice = random.choice(board.get_empty_squares())
        board.move(choice[0], choice[1], sim_player)
        
        # Check for a win
        if (board.check_win() == None):
            sim_player = provided.switch_player(sim_player)
        else:
            return
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the 
    same dimensions as the Tic-Tac-Toe board, a board from a 
    completed game, and which player the machine player is. The 
    function should score the completed board and update the scores 
    grid. As the function updates the scores grid directly, it does 
    not return anything.
    """

    # Determine the number of needed steps and the initial row indexes
    # for the current simulation board
    steps = range(board.get_dim())
    up_index = [(0, i) for i in steps]
    
    # Step through the simuliation board, and update the list of 'scores'
    # for each move option
    for initial_square in up_index:
        for step in steps:
            row = initial_square[0] + step * 1
            col = initial_square[1]
            
            # If current player won the game, update scores accordingly
            if (board.check_win() == player):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col] -= SCORE_OTHER
                else:
                    pass
            
            # If opponent won the game, update scores accordingly
            elif (board.check_win() == provided.switch_player(player)):
                if board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col] += SCORE_OTHER
                else:
                    pass
            
            # For a tie, cruise on by...
            else:
                pass
                    
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The 
    function should find all of the empty squares with the maximum 
    score and randomly return one of them as a (row, column) tuple. 
    It is an error to call this function with a board that has no 
    empty squares (there is no possible next move), so your function 
    may do whatever it wants in that case. The case where the board 
    is full will not be tested.
    """

    # Create lists for empty squares, associated scores, and best move
    # options
    empties = board.get_empty_squares()
    emp_scores = []
    best_options = []
    
    # Get move score for each empty square on board
    for empty in empties:
        row = empty[0]
        col = empty[1]
        emp_scores.append(scores[row][col])
    
    # Determine top value of move scores for empty squares
    top_value = max(emp_scores)
    
    # Choose and return best move option
    for empty in empties:
        row = empty[0]
        col = empty[1]
        if scores[row][col] == top_value:
            best_options.append(empty)
    return random.choice(best_options)
        
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine 
    player is, and the number of trials to run. The function should 
    use the Monte Carlo simulation return a move for the machine 
    player in the form of a (row, column) tuple. Be sure to use the
    other functions you have written!
    """
    
    # Create list for tracking scores of simulated moves
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    
    # Run simulations and return best move
    for dummy in range(trials):
        sim_board = board.clone()
        mc_trial(sim_board, player)
        mc_update_scores(scores, sim_board, player)
    best_move = get_best_move(board, scores)
    return best_move

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
