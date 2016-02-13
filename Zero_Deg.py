# -*- coding: utf-8 -*-
"""
Examines a given undirected graph, and returns the set of nodes from said
graph that have degree 0

@author: netcdk
"""

def zero_deg(matrix):
    z_degs = set()
    
    for i in matrix:
        no_degs = True
        for j in matrix:
            if j in i:
                no_degs = False
                break
        if no_degs == True:
            z_degs.add(i)
    return z_degs
