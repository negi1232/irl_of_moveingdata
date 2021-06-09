from itertools import count
import numpy as np
import osmnx as ox
import networkx  as nx
import sqlite3
import os
import tqdm
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def probs_dic(nodedict,):
    policy=dict()    
    for i in range(len(list(G.nodes))):
        #print(i, list(nx.all_neighbors(G, list(G.nodes)[i])),G.degree(list(G.nodes)[i]))
        nodelist=list(nx.all_neighbors(G, list(G.nodes)[i]))
        st=list()
        for j in list(nx.all_neighbors(G, list(G.nodes)[i])):
            st.append(nodedict[j])
        policy[nodedict[list(G.nodes)[i]]]=st
    return policy


if __name__ == '__main__':      
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    print(probs_dic(G))
