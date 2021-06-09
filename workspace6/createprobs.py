from itertools import count
import numpy as np
import osmnx as ox
import networkx  as nx
import sqlite3
import os
import tqdm
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def probs_dic(G,nodedict):
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
    


def policy_SQL():
    insertlist=[]
    dbname = 'log.db'
    con = sqlite3.connect(dbname) #DBに接続
    cur = con.cursor()#カーソルを使いやすいように代入
    cur.execute('CREATE TABLE IF NOT EXISTS policy(seq INTEGER PRIMARY KEY AUTOINCREMENT,origin INTEGER,conect0 INTEGER,conect1 INTEGER,conect2 INTEGER,conect3 INTEGER,conect4 INTEGER,conect5 INTEGER,conect6 INTEGER,conect7 INTEGER,conect8 INTEGER,conect9 INTEGER,Choices INTEGER)')
    insert_sql='INSERT INTO policy(origin,conect0,conect1,conect2,conect3,conect4,conect5,conect6,conect7,conect8,conect9,Choices) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'
    #policy=
    #policy = np.zeros([n_states, n_actions])
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    #print(list(G.nodes))
    insertlist=list()
    count
    for i in range(len(list(G.nodes))):
        st=list()
        print(i, list(nx.all_neighbors(G, list(G.nodes)[i])),G.degree(list(G.nodes)[i]))
        nodelist=list(nx.all_neighbors(G, list(G.nodes)[i]))
        st.append(list(G.nodes)[i])#add origin
        for j in range(10):#最大ノード数を10と仮定
            try:
                nodelist[j]
                st.append(nodelist[j])
            except:
                st.append("null")
        st.append(G.degree(list(G.nodes)[i]))
        insertlist.append(st)
        if (i + 1) % 1000 == 0:
            #print(len(insertlist))
            cur.executemany(insert_sql, insertlist)
            con.commit()
            insertlist = []
        
    cur.executemany(insert_sql, insertlist)
    con.commit()
    #fig, ax = ox.plot_graph(G)