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
    create_sql='CREATE TABLE IF NOT EXISTS reward(seq INTEGER PRIMARY KEY AUTOINCREMENT,node INTEGER,reward0 INTEGER,reward1 INTEGER,reward2 INTEGER,reward3 INTEGER,reward4 INTEGER,reward5 INTEGER,reward6 INTEGER,reward7 INTEGER,reward8 INTEGER,reward9 INTEGER,reward10 INTEGER,reward11 INTEGER,reward12 INTEGER,reward13 INTEGER,reward14 INTEGER,reward15 INTEGER,reward16 INTEGER,reward17 INTEGER,reward18 INTEGER,reward19 INTEGER,reward20 INTEGER,reward21 INTEGER,reward22 INTEGER,reward23 INTEGER)'
    cur.execute(create_sql)
    insert_sql='INSERT INTO reward(node,reward0,reward1,reward2,reward3,reward4,reward5,reward6,reward7,reward8,reward9,reward10,reward11,reward12,reward13,reward14,reward15,reward16,reward17,reward18,reward19,reward20,reward21,reward22,reward23) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    insertlist=list()
    #for i in range(len(reward[0])):
    for i in range(8000):
        st=list()
        #print(i,revnodedict[i],reward[i])
        insertlist.append([revnodedict[i],reward[0][i],reward[1][i],reward[2][i],reward[3][i],reward[4][i],reward[5][i],reward[6][i],reward[7][i],reward[8][i],reward[9][i],reward[10][i],reward[11][i],reward[12][i],reward[13][i],reward[14][i],reward[15][i],reward[16][i],reward[17][i],reward[18][i],reward[19][i],reward[20][i],reward[21][i],reward[22][i],reward[23][i]])
        if (i + 1) % 1000 == 0:
                #print(len(insertlist))
                cur.executemany(insert_sql, insertlist)
                con.commit()
                insertlist = []
        
    cur.executemany(insert_sql, insertlist)
    con.commit()
if __name__ == '__main__':
    save()