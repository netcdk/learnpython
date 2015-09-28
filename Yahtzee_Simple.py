"""
Planner for Yahtzee by CDK
Written on CodeSkulptor.org
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor, random
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    # Create a target set for scores
    scores = []
    
    # Calculate possible scores for the given hand
    for dice_value in hand:
        scores.append(hand.count(dice_value) * dice_value)
    
    # Return the max score for the given hand
    return max(scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # Create a target set for expect_value
    ex_val = []
    
    # Generate sequences of potential/new die value based on free dice 
    new_dice = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)

    # Score hands of held + potential new dice
    for die in new_dice:
        ex_val.append(score(held_dice + die))
    
    # Return a float of expected value
    return float(sum(ex_val)) / len(ex_val)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    # Create empty set to contain hold options, starting with the
    # option to hold no die
    hold_set = set([()])
        
    # Iterate through each die in hand
    for die_value in hand:
        
        temp_set = set()
        temp_set.update(hold_set)
        
        # Iterate through existing tuples in copy of hold_set
        for partial_sequence in hold_set:
                      
            # Combine values of existing tuples with current die_value
            new_sequence = list(partial_sequence)
            new_sequence.append(die_value)
            
            # Sort new_sequence
            new_sequence = sorted(new_sequence)
            
            # Check to see if sorted new_sequence is already in temp_set,
            # and add it if not already there
            temp_set.add(tuple(new_sequence))
        
        # Update hold_set with new options to hold
        hold_set = temp_set

    return hold_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    current_value = 0
    
    for hold in gen_all_holds(hand):
        value = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if value > current_value:
            current_value = value
            result = (current_value, hold)
    
    return result


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 5, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(expected_value)