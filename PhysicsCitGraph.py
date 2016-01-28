# -*- coding: utf-8 -*-
"""
Normalization and plotting of in-degree distribution of 
citation graph data for Algorithmic Thinking P1

@author: netcdk
"""

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import DegDistroGraphsALT2 as ddg
import matplotlib.pyplot as plt

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

# Run in-degree distriubtion on citation graph
cit_idd = ddg.in_degree_distribution(citation_graph)


# Function to normalize in-degree distribution
def normal_idd(idd):
    total_values =  sum(idd.values())   
    norm_idd = {}
    for key in idd.keys():
        norm_idd[key] = (float(idd[key]) / float(total_values))
    return norm_idd


# Run in-degree distribution on citation graph data
n_cit_idd = normal_idd(cit_idd)


# Function to remove a given element from dictionary
def remove_elem(dictionary, key):
    copy_dict = dict(dictionary)
    del copy_dict[key]
    return copy_dict


# Remove nodes with in-degree of zero
nci_nozero = remove_elem(n_cit_idd, 0)


# Plot log/log of the points of the normalized distribution
plt.loglog(nci_nozero.keys(), nci_nozero.values(), linestyle='None', marker=".")
plt.xlabel("log10(number of in-degrees)")
plt.ylabel("log10(normalized distribution of in-degree frequency)")
plt.title("In-degree distribution of citation graph")
plt.savefig("idd citation graph")