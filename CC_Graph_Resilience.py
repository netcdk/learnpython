# -*- coding: utf-8 -*-
"""
Project component of Module 2 for Algorithmic Thinking P1: 
- Implement breadth-first search
- Compute the set of connected components (CCs) of an undirected graph as well
as determine the size of its largest connected component
- Computes the resilience of a graph (measured by the size of its largest
connected component) as a sequence of nodes are deleted from the graph

@author: netcdk
"""

# imports
from collections import deque
import random

# testing set
EX_GRAPH0 = { 0 : set([1]),
            1 : set([0]),
            2 : set([])}


EX_GRAPH1 = { 0 : set([1,3,5]),
            1 : set([0]),
            2 : set([4]),
            3 : set([0]),
            4 : set([2]),
            5 : set([0,6]),
            6 : set([5])}
            
EX_GRAPH2 = { 0 : set([1,2]),
            1 : set([0,2]),
            2 : set([0,1]),
            3 : set([4,5,6]),
            4 : set([3,5,6]),
            5 : set([3,4,6]),
            6 : set([3,4,5])}


def bfs_visited(ugraph, start_node):
    """
    Function that takes an undirected graph and a starting node and returns 
    the set consisting of all nodes that are visited by a breadth-first search
    that starts at the given start node
    """
    visited_nodes = set([start_node])
    
    queue = deque()
    queue.append(start_node)
    
    while len(queue) > 0:
        node_x = queue.popleft()
        for next_node in ugraph[node_x]:
            if next_node not in visited_nodes:
                visited_nodes.add(next_node)
                queue.append(next_node)

    return visited_nodes


def cc_visited(ugraph):
    """
    Function that takes an undirected graph and returns a list of sets, where
    each set consists of all (and only) the nodes in a connected component,
    and there is exactly one set in the list for each connected component in
    given undirected graph (and nothing else).
    """
    remaining_nodes = ugraph.keys()
    remaining_nodes = set(remaining_nodes)
    
    connected_comps = []
    
    while len(remaining_nodes) > 0:
        node_x = random.sample(remaining_nodes, 1)[0]
        visited_nodes = bfs_visited(ugraph, node_x)
        connected_comps.append(visited_nodes)
        for node in visited_nodes:
            remaining_nodes.remove(node)
    
    return connected_comps
    
def largest_cc_size(ugraph):
    """
    Function that takes an undirected graph and returns the size (an integer)
    of the largest connected component in the given undirected graph.
    """
    largest = 0
    connected_comps = cc_visited(ugraph)
    
    for component in connected_comps:
        if len(component) > largest:
            largest = len(component)
    
    return largest

def compute_resilience(ugraph, attack_order):
    """
    Function that takes an undirected graph and a list of nodes (attack_order),
    and iterates through the nodes in attack_order. For each node in the list,
    function removes the given node and its edges from the graph and then
    computes the size of the largest connected component for the resulting
    graph.
    """
    copy_ugraph = ugraph.copy()

    sizes = []
    sizes.append(largest_cc_size(copy_ugraph))
    
    for node in attack_order:
        copy_ugraph.pop(node)
        for node_sets in copy_ugraph:
            copy_ugraph[node_sets].discard(node)
        sizes.append(largest_cc_size(copy_ugraph))
    
    return sizes

## testing
# print bfs_visited(EX_GRAPH1, 6)
# print cc_visited(EX_GRAPH1)
# print cc_visited(EX_GRAPH2)