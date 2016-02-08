# -*- coding: utf-8 -*-
"""
Generator of DPA graphs, with input of number of nodes 
and probability. Graphing, too!

@author: netcdk
"""

import random
import RandGraphGen as rgg
import DegDistroGraphsALT2 as ddg
import matplotlib.pyplot as plt


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes     
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]   
   
   
    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
        
        
def dpa_gen(num_nodes, exist_nodes):

# Generate a fully connected directed graph based on existing nodes input
    graph_base = rgg.Dir_Graph(exist_nodes, 1)
    digraph = graph_base.gen_edges()
    new_graph = digraph.copy()
    trial = DPATrial(exist_nodes)
    
    # Generate and connect additional nodes
    for new_node in xrange(exist_nodes, num_nodes):  
        connect = trial.run_trial(exist_nodes)
        new_graph[new_node] = connect
    
    #return direction DPA graph
    return new_graph

        
# Test graphs for DPA
dpa_graph = dpa_gen(27770, 12)
#print dpa_graph

# Run in-degree distriubtion on randomly generated graph
dpa_idd = ddg.in_degree_distribution(dpa_graph)
#print dpa_idd

# Function to normalize in-degree distribution
def normal_idd(idd):
    total_values =  sum(idd.values())   
    norm_idd = {}
    for key in idd.keys():
        norm_idd[key] = (float(idd[key]) / float(total_values))
    return norm_idd


# Run in-degree distribution on citation graph data
n_dpa_idd = normal_idd(dpa_idd)
#print n_dpa_idd

# Function to remove a given element from dictionary
def remove_elem(dictionary, key):
    if key not in dictionary.keys():
        return dictionary
    else:
        copy_dict = dict(dictionary)
        del copy_dict[key]
        return copy_dict


# Remove nodes with in-degree of zero
dpa_nozero = remove_elem(n_dpa_idd, 0)
#print dpa_nozero

# Plot log/log of the points of the normalized distribution
plt.loglog(dpa_nozero.keys(), dpa_nozero.values(), linestyle='None', marker=".")
plt.xlabel("log10(number of in-degrees)")
plt.ylabel("log10(normalized distribution of in-degree frequency)")
plt.title("In-degree distribution of DPA graph")
plt.savefig("dpa graph")