from maxent_irl import Reward
import numpy as np
import tqdm
import sqlite3
import os


def save(reward,revnodedict):#μ0(s0)を計算
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    insertlist=[]
    dbname = 'log.db'
    con = sqlite3.connect(dbname) #DBに接続
    cur = con.cursor()#カーソルを使いやすいように代入
    create_sql='CREATE TABLE IF NOT EXISTS reward(seq INTEGER PRIMARY KEY AUTOINCREMENT,node INTEGER,reward node INTEGER)'
    cur.execute(create_sql)
    insert_sql='INSERT INTO reward(node,reward) VALUES(?,?)'
    insertlist=list()
    for i in range(len(reward)):
        st=list()
        print(i,revnodedict[i],reward[i])
        insertlist.append([revnodedict[i],reward[i]])
        if (i + 1) % 1000 == 0:
                #print(len(insertlist))
                cur.executemany(insert_sql, insertlist)
                con.commit()
                insertlist = []
        
    cur.executemany(insert_sql, insertlist)
    con.commit()
if __name__ == '__main__':
    save()