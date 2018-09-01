import wikidriver as wkd 
import matplotlib.pyplot as plt
import networkx as nx
from relatedness import *

def draw_network(network, location=None):
    """ Displays in an interactive window a visualization of the graph underlying the specified Semantic_Network.
    """
    graph = network.graph
    draw_graph(graph, location)

def draw_graph(graph, location=None):
    """ Displays in an interactive window a visualization of the specifed graph.
    """
    positions = nx.spring_layout(graph)
    labels = get_capacity_dict(graph)
    plt.clf()
    nx.draw(graph, positions)
    nx.draw_networkx_edge_labels(graph, positions, edge_labels=labels)
    if location is None:
        plt.ion()
        plt.show()
    else:
        plt.savefig(location)

def build_new_network(topic, depth, fileName):
	newNetwork = wkd.build_network(topic, depth)
	newNetwork.save_to_file(fileName)

print(wkd.extract_normalized_links('Calculus'))
print('   ')
print(wkd.extract_normalized_links(wkd.extract_normalized_links('Calculus')[2]))
print('   ')
print(wkd.extract_normalized_links(wkd.extract_normalized_links('Calculus')[6]))
'''
try:
    network_edgeFile = 'semanticNet.txt'
    calculusNetwork = Semantic_Network(network_edgeFile)
    relatedness = calculusNetwork.calc_relatedness('Calculus', 'Eastern Europe')
    draw_network(calculusNetwork)
    input()
except FileNotFoundError: #if there is no edgelist file
	build_new_network('Calculus', 1, network_edgeFile)	
    '''
