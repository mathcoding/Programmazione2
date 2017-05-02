# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:38:45 2017

@author: gualandi
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def MakeSyntethicData(n=100, seed=13, Plot=False):
    np.random.seed(seed)
    x1 = np.random.normal(2, 1.8, n)
    y1 = np.random.normal(6, 1.8, n)  
    
    m = 20
    x2 = np.random.normal(4, 0.8, max(n, n-m))
    y2 = np.random.normal(3, 0.8, max(n, n-m))

    if n > m:
        x2 = np.append(x2, np.random.normal(10, 0.5, 20))
        y2 = np.append(y2, np.random.normal(0, 0.5, 20))

    # Return data    
    X = []
    Y = []
    for x,y in zip(x1,y1):
        X.append((x,y))
        Y.append(0)  # 0 = blue

    for x,y in zip(x2,y2):
        X.append((x,y))
        Y.append(1)  # 1 = red

    if Plot:
        # Disegna il plot
        fig, ax = plt.subplots(figsize=(13, 7))
        
        ax.scatter(x1, y1, alpha=0.5, c='blue')
        ax.scatter(x2, y2, alpha=0.5, c='red')
        
        ax.legend(('Blue=0', 'Red=1'))
        plt.show()
        
    return X, Y

#------------------------------------------
#              MAIN ENTRY POINT
#------------------------------------------
if __name__ == "__main__":
    x_train, y_train = MakeSyntethicData(100, Plot=True)
    
    # PRIMA DI FARE QUESTO ESERCIZIO, STUDIARE IL TUTORIAL:
    # http://scikit-learn.org/stable/modules/neural_networks_supervised.html
    #
    # ESERCIZIO DA FARE: PROVARE I DIVERSI PARAMETRI DI QUESTA CLASSE
    # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    ann = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(4), random_state=1)
    
    ann.fit(x_train, y_train)
    
    x_test, y_test = MakeSyntethicData(20, seed=21)
    y_pred = ann.predict(x_test)
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    
    # CONTROLLO DEI PESI
    W1 = ann.coefs_[0]
    W0 = ann.intercepts_
    print("W1:", W1)
    print("W1:", W0[0])
    Z1 = [max(0, W0[0][i]+W1[0][i]*x_test[0][0]+W1[1][i]*x_test[0][1]) for i in range(4)]
    print(Z1)
    
    W2 = ann.coefs_[1]
    W0 = ann.intercepts_
    print("W2:", W2)
    print("W0:", W0[1])
    
    print(W0[1][0]+sum([W2[i][0]*Z1[i] for i in range(4)]))
    print(y_test[0])