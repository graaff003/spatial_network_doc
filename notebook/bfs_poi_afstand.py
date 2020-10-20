#!/usr/bin/env python
# coding: utf-8

# # Distance Matrix Calculation

# This script is based on the code in the following git repository:
# https://git.datapunt.amsterdam.nl/Data-Oplossingen/waardecontainers_afval/blob/master/python/netwerk_analyse/afval_module.py
#
# The script calculates a distance matrix with a threshold using Breath First Search algorithm. A graph is build based on nodes and edges (walking distance as weight) retrieved from Postgres DB tables. The threshold can be set as parameter in the get_distance_matrix function and the 'type' node that is used as from node can be set in the create_graph function where all poi's are retrieved.
#
# ToDo: error handling, type checking, completeness checking

# Imports
import heapq
from collections import deque
import collections
import csv
import datetime
import math
import re
import os
import pandas as pd
from getpass import getpass
from decimal import *


# get the data from a geodata frame
def get_data(p_obj_type, p_gdf):
    #
    if p_obj_type == 'node':
        print('node')
        # node_id, st_astext(geometrie)
        l_data = p_gdf[['node_id','geometry']]

    elif p_obj_type == 'edge':
        print('edge')
        #s1_afv_edges, node_id__startpoint, node_id__endpoint, weight
        l_data = p_gdf

    elif p_obj_type == 'poi':
        print('poi')
        # np.node_id,np.poi_id, poi_type {to_poi (bag_poi) , from_poi}
        l_data = p_gdf

    else:
        print ('obj_type not recognized')


    return l_data


# # Define Classes
class Queue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements[1]


class SimpleQueue(Queue):
    """
        basic simple queue, used for breath first search algerithm
    """
    def __init__(self):
        self.elements = deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

class Graph:
    def __init__(self):
        self.nodes = dict()
        self.id_point_map = {}
        self.objects = []
        self.to_nodes_map = {}
        self.from_nodes_map = {}
        self.timestamp = datetime.datetime.now()

    def get_nodepoint_by_id(self, node_id):
        return self.id_point_map.get(node_id)


class Node:
    def __init__(self, point_id, coords, parent):
        self.point_id = point_id
        self.coords = coords
        self.edges = []
        self.type = 'general'
        self.obj_id = ''
        self.parent = parent

        parent.nodes[self.point_id] = self

    def __str__(self):
        return 'node:\n' + str(self.point_id) + "|" + self.type + "|" + str(len(self.edges))


class Edge:
    def __init__(self, edge_id, from_node, to_node, length):
        self.edge_id = edge_id
        self.from_node = from_node
        self.to_node = to_node
        self.length = length

    def get_to_point(self, point_id):
        if self.from_node == point_id:
            return self.to_node
        else:
            return self.from_node


# Build Graph
# poi_type_from, poi_type_to,node_data,edge_data,poi_data
def create_graph(poi_type_from, poi_type_to,node_data,edge_data,poi_data):
    """
    input:
    - dataframe nodes
    - dataframe edges
    - dataframe poi

    """
    graph = Graph()
    #
    # Retrieve all nodes for network.
    data = node_data
    i = 0
    for item in data:
        node_id, node_coords = item

        n_node = graph.nodes.get(node_id)

        if not n_node:
            Node(node_id, node_coords, graph)
            i += 1

    print('Created ', i, ' network nodes')


    # Retrieve all edges for network.
    data = edge_data
    i = 0
    for item in data:
        fid_pk, id_startpoint, id_endpoint, weight = item

        n_from = graph.nodes.get(id_startpoint)
        n_to = graph.nodes.get(id_endpoint)

        if not n_from or not n_to:
            print("[!] Could not link edge with id:", fid_pk)
            break

        #e = Edge(fid_pk, id_startpoint, id_endpoint, weight)
        e = Edge(fid_pk,id_startpoint,id_endpoint,weight)	
        n_from.edges.append(e)
        n_to.edges.append(e)

        i += 1

    print('Created ', i, ' network edges')

    # Retrieve all poi's for network. 
    data = poi_data
    for item in data:
        #node_id, poi_id, poi_type = item
        node_id,poi_id,poi_type = item

        node = graph.nodes.get(node_id)
        if not node:
            print('\n[!] Missed a node:', item)
        else:
            node.type = poi_type
            node.obj_id = poi_id
            node.parent.id_point_map[poi_id] = node_id
            if node.type == poi_type_from:
                graph.from_nodes_map[node_id] = node
            if node.type == poi_type_to:
                graph.to_nodes_map[node_id] = node

    print('\nNumber of begin nodes:', len(graph.from_nodes_map))
    print('Number of end nodes:', len(graph.to_nodes_map))
    return graph


# # Calculate Distance Matrix
def get_distance_matrix(graph, threshold):
    nodes = graph.from_nodes_map
    result = []
    for node in nodes:
        data = breadth_first_search(graph, node, threshold)
        for x, y in data.items():
            if x in graph.to_nodes_map:
                result.append([node, x, y])
    return result


def breadth_first_search(graph, p1, threshold):
    """
        breadth first search algorithm. Searches all nodes in the network within threshold distance of the input
        node.
    :param p1: Input node identification 'POINT(xxxx.xxx yyyy.yyy)'
    :param threshold: Maximum search distance
    :return: dict of nodes reached with max range, including cost to reach the node
    """
    frontier = SimpleQueue()
    frontier.put(p1)
    visited = dict()
    visited[p1] = True
    cost_per_node = dict()
    cost_per_node[p1] = Decimal(0.0)

    # check if there are any options left
    while not frontier.empty():
        # get first of the frontier locations, to move from
        current = frontier.get()
        # from this posisiton, check the next options in the graph
        c_object = graph.nodes[current]
        for edge in c_object.edges:
            out = edge.get_to_point(current)
            # check if i have already been there
            if not out in visited:
                visited[out] = True  # now we have been there
                cost_to_get_here = cost_per_node[current] + Decimal(edge.length)
                if cost_to_get_here <= threshold:
                    cost_per_node[out] = cost_to_get_here
                    frontier.put(out)  # update the frontier, to continue from there

    return cost_per_node


# # Main Function
def network_run(p_node_data, p_edge_data, p_poi_data,poi_type_from, poi_type_to, cutoff):

    # Retrieve the nessesary data
    node_data = get_data('node',p_node_data)
    edge_data = get_data('edge',p_edge_data)
    poi_data = get_data('poi',p_poi_data)

    # return the graph 
    graph = create_graph(poi_type_from, poi_type_to,node_data,edge_data,poi_data)

    # return the matrix
    data = get_distance_matrix(graph, threshold=cutoff)


    #print ('Start conversion to dataframe: ',str(startDT))
    data_df = pd.DataFrame.from_records(data, columns=['van_node_id', 'naar_node_id', 'afstand'])
    #print ('number of rows in frame:', len(data_df))

    # get file location
    csv_afv_poi_afstand = os.environ.get('out_csv')

    #print ('Start writing to csv: ',str(startDT))
    data_df.to_csv(csv_afv_poi_afstand,index=False,header=True,sep=';')
    #print ('Ended writing to csv: ',str(datetime.datetime.now() - startDT))


    return data_df

"""
if __name__ == '__main__':
    # call the procedure from poi_type , to_poi_type, cutoff distance
    network_run('ov_halte', 'bag_poi', 1000)
"""