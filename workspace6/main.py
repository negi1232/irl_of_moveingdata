import os
import sqlite3
from sys import path_hooks
import osmnx as ox
import networkx  as nx
import numpy as np
import createprobs
import createpolicy
import createtrajectories
import createdic
from value_iteration import ValueIteration
from maxent_irl import Reward, StateVisitationFrequency, compute_experts_feature
import ressave
import matplotlib.pyplot as plt
from tqdm import tqdm
n_epochs=1
epsilon=0.1
gamma=0.99
learning_rate=0.5
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    G = ox.graph_from_bbox(  35.706, 35.6614, 140.0843, 139.9987,network_type='drive')
    nodedict,revnodedict=createdic.dic(G)
    trajectories,max,min=createtrajectories.trajectories(nodedict)
    
    #print(trajectories)
    
    nS=len(list(G.nodes))
    probs=createprobs.probs_dic(G,nodedict)
    svf = StateVisitationFrequency(nS,nodedict,probs,max,min)#インスタンスを作成し、状態の数,アクションの数,タイル間で移動できるかの辞書を入力
    #print(svf)
    experts_feature = compute_experts_feature(nS, trajectories)
    feature_matrix = np.eye(nS)
    reward_function = Reward(nS)
    value_iteration = ValueIteration(nS, 10, probs)
    for i in  tqdm(range(n_epochs)):#20回ループする
        pass
        V, policy = value_iteration(gamma, epsilon, reward_function)
        #重要訪れたことのない地点に報酬が発生した理由１ 訪れたことのない地点でのpolicyが発散したから
        pass
        # for i in V:
        #     print(i)
        # print("////////////////////////////")
        P = svf(policy, trajectories)

        pass
        # for i in policy:
        #     print(i)
        grad = experts_feature - feature_matrix.T.dot(P)
        #There is a problem in generating the action trajectory
        


        # for i in range(len(P)):
        #     #if grad[i] !=0:
        #     print(i,P[i])
        # print("////////////////////////////")

        # for i in range(len(experts_feature)):
        #     #if grad[i] !=0:
        #     print(i,experts_feature[i])
        # print("////////////////////////////")

        # for i in range(len(feature_matrix.T.dot(P))):
        #     #if grad[i] !=0:
        #     print(i,feature_matrix.T.dot(P)[i])
        # print("////////////////////////////")

        # for i in range(len(grad)):
        #     #if grad[i] !=0:
        #     print(i,grad[i])
        # print("////////////////////////////")


        reward_function.update(learning_rate * grad)
        
        pass
    
    reward=reward_function(feature_matrix)
    
    ressave.save(reward,revnodedict)
    # st=np.zeros(10000)
    # plt.cla()
    # aa=0
    # for i in range(10000):
    #     try:
    #         reward[i]
    #         st[i]=reward[i]
    #         #print(reward[i])
    #         if reward[i]>5:
    #             st[i]=3
    #         if reward[i]>5:
    #             print(revnodedict[i],reward[i])
            
    #     except:
    #         pass
    #node_color = [node["color"] for node in G.nodes.values()]
    # pass
    # 
    # plt.cla()
    # plt.pcolor(st.reshape(100, 100)[::-1, :])
    # plt.colorbar()
    # plt.show()
    # pass