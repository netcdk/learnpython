"""
Algorithmic Thinking P1
Degree Distributions for Graphs (ALT CODE)
Written by netcdk on codeskulptor.org
"""

# Three graph constants, as examples
EX_GRAPH0 = {0: set([1, 2]),
             1: set(),
             2: set()}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set()}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set(),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
    Function that takes a number of nodes and returns
    a dictionary corresponding to a complete directed graph
    with the specified number of nodes
    """
    digraph = {}
    if num_nodes < 1:
        return digraph
    else:
        edges = set(range(num_nodes))
        for node in range(num_nodes):
            digraph[node] = edges.difference(set([node]))
        return digraph


def compute_in_degrees(digraph):
    """
    Function that takes a directed graph digraph (represented as
    a dictionary), computes the in-degrees for the nodes in
    the graph, and returns a dictionary with the same set of keys
    (nodes) as digraph whose corresponding values are the number
    of edges whose head matches a particular node.
    """
    values = []
    cid = {}
    for key in digraph.keys():
        values += list(digraph[key])
        cid[key] = 0
    
    for value in values:
        cid[value] += 1
    return cid
    
#print compute_in_degrees(EX_GRAPH0)
#print compute_in_degrees(EX_GRAPH1)
#print compute_in_degrees(EX_GRAPH2)


def in_degree_distribution(digraph):
    """
    Function that takes a directed graph digraph (represented as
    a dictionary) and computes the unnormalized distribution of
    the in-degrees of the graph. The function returns a dictionary
    whose keys correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree is the
    number of nodes with that in-degree. In-degrees with no
    corresponding nodes in the graph are not included in the
    dictionary.
    """
    #return dict(collections.Counter((compute_in_degrees(digraph)).values()))
    idd = {}
    in_degrees = (compute_in_degrees(digraph)).values()
    for degree in in_degrees:
        if degree in idd:
            pass
        else:
            idd[degree] = in_degrees.count(degree)
    return idd
    
#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH2)
    
    
def compute_out_degrees(digraph):
    """
    Function that takes a directed graph digraph (represented as
    a dictionary), computes the in-degrees for the nodes in
    the graph, and returns a dictionary with the same set of keys
    (nodes) as digraph whose corresponding values are the number
    of edges whose head matches a particular node.
    """
    cod = {}
    for key in digraph.keys():       
        cod[key]= len(list(digraph[key]))

    return cod

#print compute_out_degrees(EX_GRAPH0)
#print compute_out_degrees(EX_GRAPH1)
#print compute_out_degrees(EX_GRAPH2)


def out_degree_distribution(digraph):
    """
    Function that takes a directed graph digraph (represented as
    a dictionary) and computes the unnormalized distribution of
    the in-degrees of the graph. The function returns a dictionary
    whose keys correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree is the
    number of nodes with that in-degree. In-degrees with no
    corresponding nodes in the graph are not included in the
    dictionary.
    """
    #return dict(collections.Counter((compute_in_degrees(digraph)).values()))
    odd = {}
    out_degrees = (compute_out_degrees(digraph)).values()
    for degree in out_degrees:
        if degree in odd:
            pass
        else:
            odd[degree] = out_degrees.count(degree)
    return odd
    
#print out_degree_distribution(EX_GRAPH0)
#print out_degree_distribution(EX_GRAPH1)
#print out_degree_distribution(EX_GRAPH2)