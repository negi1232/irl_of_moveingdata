from itertools import count
import numpy as np
import osmnx as ox
import networkx  as nx
import sqlite3
import os
import tqdm
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def dic(G):
    nodedict=dict()
    revnodedict=dict()
    latlotdic=dict()
    count=0
    for i in list(G.nodes):
        nodedict[i]=count
        revnodedict[count]=i
        #print(G.nodes[i]["x"],G.nodes[i]["y"])
        if i==8497360310:
            print(i)
            print(count)
        count+=1
    return nodedict,revnodedict
def latlotdic(G):
    latlotdic=dict()
    for i in list(G.nodes):
        #print(G.nodes[i]["x"],G.nodes[i]["y"])
        latlotdic[i]=[G.nodes[i]["x"],G.nodes[i]["y"]]
    return latlotdic

if __name__ == '__main__':      
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    dic(G)
    