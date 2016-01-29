# -*- coding: utf-8 -*-
"""
Algorithm ER - Generator of random undirected graphs, with
input of nodes and probability.

@author: netcdk
"""

import random

class Undir_Graph:
    def __init__(self, nodes, probability):
        self.nodes = nodes
        self.prob = probability
        self.graph = {}
    
    def get_nodes(self):
        return self.nodes
        
    def get_prob(self):
        return self.prob
        
    def get_graph(self):
        return self.graph
    
    def gen_edges(self.nodes, self.prob):
        for i in self.nodes:
            for j in self.nodes:
                if j != i:
                    chance = random.random()
                    if chance < self.prob:
                        