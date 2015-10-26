"""
Student code for Word Wrangler game
Written on CodeSkulptor.org
by CDK
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    unique = []
    
    for item in list1:
        if item not in unique:
            unique.append(item)
    
    return unique

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    
    intersections = []
    
    # Simple approach
    for item in list1:
        if item in list2:
            intersections.append(item)

#    # Approach recommended by forums for improved performance
#    idx1 = 0
#    idx2 = 0
#    while (idx1 < len(list1)) and (idx2 < len(list2)):
#        if (list1[idx1] == list2[idx2]):
#            intersections.append(list1[idx1])
#            idx1 += 1
#            idx2 += 1
#        elif (list1[idx1] < list2[idx2]):
#            idx1 += 1
#        else:
#            idx2 += 1    

    return intersections

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    
    # Create "copy" lists and target "merged" list
    l1copy = list1[:]
    l2copy = list2[:]
    
    merged = []
    
    # While both lists have at least one item, compare lowest values 
    # between "copy" lists, add lowest value to new "merged" list, 
    # and remove value from appropriate "copy" list
    while (len(l1copy) > 0) and (len(l2copy) > 0):
        if l1copy[0] == l2copy[0]:
            merged.append(l1copy.pop(0))
        elif l1copy[0] > l2copy[0]:
            merged.append(l2copy.pop(0))
        else:
            merged.append(l1copy.pop(0))
    
    # Add in the remaining items of whichever "copy" list (in any) 
    # has len > 0
    merged += l1copy + l2copy
       
    return merged
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
#    # ALTERNATIVE OPTION - Does not use "merge" function
#
#    # Immediately return list if one item or less in list
#    if len(list1) <= 1:
#        return list1
#    
#    # Determine pivot, and sort recursively
#    else:
#        pivot = list1[0]
#        lesser = [num for num in list1 if num < pivot]
#        pivots = [num for num in list1 if num == pivot]
#        greater = [num for num in list1 if num > pivot]
#        return merge_sort(lesser) + pivots + merge_sort(greater)
    
    # SELECTED OPTION - Uses "merge" function, per instructions
    
    # Create targets for below and above the midpoint
    lesser = []
    greater = []
    
    # Immediately return list if one item or less in list
    if (len(list1) <= 1):
        return list1
    
    # Determine midpoint, and start sorting recursively
    
    mid = len(list1) / 2
    lesser = merge_sort(list1[:mid])
    greater = merge_sort(list1[mid:])
    
    return merge(lesser, greater)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
    # Immediately return list if one item or less in list
    if len(word) < 1:
        return [word]
    
    # Split word into two parts
    first = word[0]
    rest = word[1:]
    
    # Generate all strings for rest
    rest_strings = gen_all_strings(rest)
    
    # Generate new strings based on "rest_strings"
    new_strings = []
    for string in rest_strings:
        for index in range(len(string) + 1):
            new_strings.append(string[:index] + first + string[index:])
        
    return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    
    return netfile.read()

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    
