import math
import numpy as np
import xml.etree.ElementTree as ET
import vrplib

def readFile(path):
    vrplib.download_instance(path, f'instances/{path}.vrp')
    return vrplib.read_instance(f"instances/{path}.vrp")

# fileInst = FileRead("A-n60-k9")
# a = fileInst.instanceTaker()
# print(a["capacity"])

    
def distance(p1, p2):
    """
    Calculate the Euclidean distance between two points.
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distance_matrix(coords):
    """
    Calculate the distance matrix for a list of coordinates.
    """
    n = len(coords)
    dist_matrix = [[0.0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist_matrix[i][j] = distance(coords[i], coords[j])
            dist_matrix[j][i] = dist_matrix[i][j]
    return dist_matrix

def input(path):
    tree = ET.parse(f'instances_CVRP/{path}')
    root = tree.getroot()
    nodes = []
    demands = []
    name = root.find('info/name').text
    k = int(name[-2:])
    n = int(name[3:5])
    c = float(root.find('fleet/vehicle_profile/capacity').text)
    # print(k, n, c)
    for node in root.findall('network/nodes/node'):
        node_id = int(node.get('id'))
        cx = float(node.find('cx').text)
        cy = float(node.find('cy').text)
        nodes.append((cx, cy))
    for node in root.findall('requests/request'):
        node_id = int(node.get('id'))
        r = float(node.find('quantity').text)
        demands.append(r)
    return np.array(distance_matrix(nodes)), demands, k, n - 1, c

# print(input('A-n32-k05.xml'))
# matrix = distance_matrix(nodes)
# print(matrix)