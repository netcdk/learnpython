# -*- coding: utf-8 -*-
"""
Generator of random undirected or directed graphs, with
input of number of nodes and probability. Graphing, too!

@author: netcdk
"""

import random
import DegDistroGraphsALT2 as ddg
import matplotlib.pyplot as plt

class Undir_Graph:
    def __init__(self, num_nodes, probability):
        self.nodes = range(num_nodes)        
        self.prob = probability
        self.graph = {}
        for node in self.nodes:
            self.graph[node] = set([])
        
    def get_prob(self):
        return self.prob
    
    def get_nodes(self):
        return self.graph.keys()
    
    def get_edges(self):
        return self.graph.values()
    
    def get_graph(self):
        return self.graph
    
    def gen_edges(self):
        for i in self.nodes:
            for j in self.nodes:               
                if j == i or set([j]).issubset(self.graph[i]):
                    pass
                else:     
                    chance = random.random()
                    if chance < self.prob:
                        self.graph[i].add(j)
                        self.graph[j].add(i)
        return self.graph

class Dir_Graph:
    def __init__(self, num_nodes, probability):
        self.nodes = range(num_nodes)        
        self.prob = probability
        self.graph = {}
        for node in self.nodes:
            self.graph[node] = set([])
        
    def get_prob(self):
        return self.prob
    
    def get_nodes(self):
        return self.graph.keys()
    
    def get_edges(self):
        return self.graph.values()
    
    def get_graph(self):
        return self.graph
    
    def gen_edges(self):
        for i in self.nodes:
            for j in self.nodes:               
                if j == i:
                    pass
                else:     
                    chance = random.random()
                    if chance < self.prob:
                        self.graph[i].add(j)
        return self.graph

# Test graphs
#dir_graph1000 = Dir_Graph(1000, .5)
#dir_graph1000.gen_edges()

# Run in-degree distriubtion on randomly generated graph
#dg1000_idd = ddg.in_degree_distribution(dir_graph1000.get_graph())


# Function to normalize in-degree distribution
def normal_idd(idd):
    total_values =  sum(idd.values())   
    norm_idd = {}
    for key in idd.keys():
        norm_idd[key] = (float(idd[key]) / float(total_values))
    return norm_idd


# Run in-degree distribution on citation graph data
#n_dg1000_idd = normal_idd(dg1000_idd)


# Function to remove a given element from dictionary
def remove_elem(dictionary, key):
    if key not in dictionary.keys():
        return dictionary
    else:
        copy_dict = dict(dictionary)
        del copy_dict[key]
        return copy_dict


# Remove nodes with in-degree of zero
#ndg1000_nozero = remove_elem(n_dg1000_idd, 0)


# Plot log/log of the points of the normalized distribution
#plt.loglog(ndg1000_nozero.keys(), ndg1000_nozero.values(), linestyle='None', marker=".")
#plt.xlabel("log10(number of in-degrees)")
#plt.ylabel("log10(normalized distribution of in-degree frequency)")
#plt.title("In-degree distribution of random graph")
#plt.savefig("random directed graph")

