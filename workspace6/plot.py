from maxent_irl import Reward
import numpy as np
import tqdm
import sqlite3
import os
import osmnx as ox
import folium
from folium.plugins import HeatMap
import createdic
import math


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    latlotdic=createdic.latlotdic(G)

    latitude = 35.6837
    longtude = 140.0415
    name = "津田沼"
    
    map = folium.Map(location=[latitude, longtude], zoom_start=14)
    dbname = 'log.db'
    con = sqlite3.connect(dbname) #DBに接続
    cur = con.cursor()#カーソルを使いやすいように代入
    res = cur.execute("select * from reward")
    reward=list()
    result=res.fetchall()
    for hour in range(24):
        reward=list()
        for i in result:
            reward.append([i[1],i[2+hour]])
        for step in range(1):
            #step=step/10
            map = folium.Map(location=[latitude, longtude], zoom_start=14)
            Heatlist=list()
            s=list()
            for i in reward:
                if i[1]>0:
                    lat=latlotdic[i[0]][0]
                    lot=latlotdic[i[0]][1]
                    s.append(i[1])
                    #if math.log(i[1]*1000) >=6.94:
                    if math.log(i[1]*1000) >=6.9:
                        #folium.CircleMarker([lot,lat],radius=math.log(i[1])*60,color='#3186cc',fill_color='#3186cc',).add_to(map)
                        #folium.CircleMarker([lot,lat],i[1]*10,color='#3186cc',fill_color='#3186cc',).add_to(map)
                        Heatlist.append([lot,lat, i[1]*100 ])
                        #folium.CircleMarker([lot,lat],radius=i[1],color='#3186cc',fill_color='#3186cc',).add_to(map)
                

            HeatMap(Heatlist, radius=40, blur=20).add_to(map)

            print("saveing")    
            map.save(str(hour)+".html")