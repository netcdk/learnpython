"""
Merge function for 2048 game by CDK
Written on CodeSkulptor.org
"""

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
