import numpy as np
import tqdm

class Reward:
    def __init__(self, n_features):
        self.n_features = n_features
        self.theta = np.random.uniform(size=(n_features,))
        #self.theta=np.zeros(n_features)
    def __call__(self, feature_matrix):
        if type(feature_matrix) is int:#入力された値がintであれば
            feature_matrix = np.eye(self.n_features, 1, feature_matrix).T#feature_matrixが1であれば[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]に変換スタート地点を1にしている.Tは行と列を入れ替え
        a=feature_matrix.dot(self.theta)
        #if a!=0:
        #    print("...")
        return feature_matrix.dot(self.theta)#feature_matrixとself.thetaの内積を計算しかえす

    def update(self, grad):
        self.theta += grad#θを更新θ=grad1+grad2+grad3+...+gradn


class StateVisitationFrequency:#重要そう
    def __init__(self, n_states,nodedict, probs,max,min):
        self.n_states = n_states#状態の総数
        self.probs = probs#方策
        self.max = max 
        self.min = min
        self.nodedict=nodedict

    def __call__(self, policy, trajectories):#μ0(s0)を計算
        n_states = self.n_states
        probs = self.probs
        nodedict=self.nodedict
        max = self.max
        min = self.min
        n_trajectories, n_steps = trajectories.shape#エキスパートの軌道の集合体を個別に分割
        #print(n_trajectories, n_steps)
        #return 0

        mu = np.zeros((n_steps, len(nodedict)))
        for trajectory in trajectories:
            mu[0, trajectory[0]] += 1
        mu /= n_trajectories

        state=0
        for t in   tqdm.tqdm(range(1, n_steps)):#μt(s)=∑a∈A∑s′∈Sμt−1(s′)π(a|s′)P(s|a,s′)の計算
            for action in range(10):
                for state in range(len(nodedict)):
                    try:
                        probs[state][action]
                        #print(probs[state][action])
                    except:
                        break
                    prob=1
                    for next_state in [probs[state][action]]:
                        #print(mu[t-1][state])
                        #print(probs[state][action])
                        #print(mu[t][nodedict[next_state]])
                        #print(sorted(nodedict))
                        #print("?////////////////")
                        #print(sorted(revnodedict))
                        #print(next_state)
                        #print(mu[t-1][state],policy[state][action],prob)
                        #mu[t][next_state] += mu[t-1][state] * probs[state][action] * prob
                        mu[t][next_state] += mu[t-1][state] * policy[state][action] * prob
                        

        return mu.sum(axis=0)


def compute_experts_feature(n_features, trajectories):#特徴量を計算
    n_trajectories, n_steps = trajectories.shape#10,100

    def one_hot_encoder(array):#trajectoriesを受け取る
        ncols = n_features#列(col)に16を代入
        out = np.zeros((array.size, ncols))#1行16列で初期化
        out[np.arange(array.size), array.ravel()] = 1#np.arange...➡等差数列を生成0から999までを1ずつ array.ravel ➡多次元のリストを1次元のリストにして返す 結果(1000, 16) 1行で0~16のどこにいたかを示す
        out.shape = array.shape + (ncols,)#outの配列を変更(1000, 16)から(100, 10, 16)
        return out
    
    one_hot_trajectories = one_hot_encoder(trajectories)#受け取ったエキスパートの起動を(100, 10)から(100, 10, 16)へ変換
    a=one_hot_trajectories
    b=one_hot_trajectories.sum(axis=(1))
    return one_hot_trajectories.sum(axis=(0, 1)) / n_trajectories#先に10行ごとの各アドレスへの訪問回数を合計してからまとめた100行の合計を取りn(100)で割る➡各タイルへの訪問回数の10サンプルごとの平均を返す
