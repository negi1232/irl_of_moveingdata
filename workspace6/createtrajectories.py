from itertools import count
import numpy as np
import sqlite3
import os
import tqdm
def trajectories(nodedict,starthour):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    insertlist=[]
    dbname = 'log.db'
    con = sqlite3.connect(dbname) #DBに接続
    cur = con.cursor()#カーソルを使いやすいように代入
    tableget_sql="SELECT * FROM sqlite_master WHERE type='table'"
    cur.execute(tableget_sql)
    #print(cur.fetchall())
    res=cur.fetchall()
    tables=list()
    for i in range(1,len(res)):
        if "tripdate" in res[i][1] :
            tables.append(res[i][1])
    max=min=None
    part=60#分×時
    trajectories = np.full((len(tables),part),-1)#エキスパート達の軌道を保存するリスト
    for i in range(len(tables)):
        defaultnode=5173
        search_sql="SELECT * FROM "+str(tables[i])+" WHERE hour = ? AND minute = ?"
        for hour in range(starthour,starthour+1):
            for minute in range(60):
                cur.execute(search_sql,[hour,minute])
                #print(cur.fetchone())
                try:
                    #print((hour*60)+minute,cur.fetchone()[10])
                    
                    spot=cur.fetchone()[10]
                    
                    spot=nodedict[spot]
                    defaultnode=spot
                    trajectories[i,minute]=spot
                    if max is None or max<spot:
                        max=spot
                    if min is None or min>spot:
                        min=spot

                except:
                    trajectories[i,minute]=defaultnode
                
    return trajectories,max,min#otozureteinaitennwo-1tokakukara

if __name__ == '__main__':
    trajectorie=trajectories()
    for i in trajectorie:
        print("/........................../")
        for j in i:
            print(j)