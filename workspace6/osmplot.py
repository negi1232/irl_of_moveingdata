from maxent_irl import Reward
import numpy as np
import tqdm
import sqlite3
import os
import osmnx as ox


def plot(G=None,reward=None):
    opts = {"node_size": 1, "bgcolor": "#262626", "node_color": "#426579", "edge_color": "#426579","route_color" : "cyan","orig_dest_size":25}
    routes=list()
    routecolors=list()
    colors=["#00796B","#0097A7","#0288D1","#1976D2","#303F9F"]
    for i in reward:
        routes.append([i[0]])
        step=[0.25,0.5,0.75,1.0,2.0]
        for j in range(len(step)):
            if i[1]>=step[len(step)-1]:
                routecolors.append(colors[len(step)-1])
                break
            if i[1]<=step[j]:
                routecolors.append(colors[j])
                break
                
        
        print(routes[-1],routecolors[-1])
    print("plot:start")
    fig, ax = ox.plot_graph_routes(G, routes, route_colors=routecolors, save=True, filepath="reward.png", **opts)




if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    dbname = 'log.db'
    con = sqlite3.connect(dbname) #DBに接続
    cur = con.cursor()#カーソルを使いやすいように代入
    res = cur.execute("select * from reward")
    reward=list()
    for i in res.fetchall():
        reward.append([i[1],i[2]])
    plot(G,reward)
    #fig, ax = ox.plot_graph_routes(G, routes,show=False, save=True, filepath="./output/"+str(hour)+":"+str(minute)+".png", **opts)
    print(G,reward)
    plot(G,reward)