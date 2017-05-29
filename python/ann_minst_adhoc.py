# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:03:15 2017

NOTA: COME RIFERIMENTO, SI GUARDINO LE SLIDES USATE A LEZIONE

@author: gualandi
"""

import time
import csv
import numpy as np
import math

from numpy import genfromtxt

from sklearn.metrics import accuracy_score

def ElaborateTrainingSet(data):
    """ Elaborate training set """
    X = []
    Y = []
    hist = np.zeros(10)
    n = len(data[0][1:])
    for row in data[:200]:
        X.append(np.array(np.insert(1/255*row[1:], n, 1)))
        k = int(row[0])
        Y.append(k)        
        hist[k] += 1
            
    print('Digit histogram:', hist)
    return X, Y

def ElaborateTestSet(data):
    """ Elaborate test set """
    X = []
    for row in data:
        X.append(np.array(row))
    return X

def G(x, beta, k):
    """ Output function """
    num = math.exp(x.dot(beta[k]))
    den = 0
    for l in range(len(beta)):
        den += math.exp(x.dot(beta[l]))        
    return num/den

def DeG(x, beta, k):
    """ First derivate of output function """
    g = G(x, beta, k)
    return g*(1 - g)

def Sigmoid(x):
    """ Basic activation function """
    return 1.0 / (1.0 + math.exp(-x))
 
def DevSigmoid(x):
    """ First derivate of sigmoid function """
    return Sigmoid(x)*(1 - Sigmoid(x))

def Loss(yp, yt):
    """ Loss function: Euclidian distance """
    r = 0
    for i in range(len(yp)):
        yi = [int(yt[i] == k) for k in range(10)]
        for a,b in zip(yi, yp[i]):
            r += pow(a-b, 2)
    return r

class ANN(object):
    def __init__(self, p, M, K, seed=13):
        """ Costructor method """
        self.p = p
        self.M = M
        self.K = K

        self.gamma = 0.1

        # Init the weights
        np.random.seed(seed)
        self.alpha = 0.05*np.random.rand(M, p)
        self.beta = 0.05*np.random.rand(K, M+1)

    def Predict(self, X):
        """ Predict output for input vector X """
        n = len(X)
    
        yp = []    
        
        U = np.ones(self.M+1)

        for i in range(n):
            xi = X[i]

            # Hidden layer
            for m in range(self.M):
                U[m] = Sigmoid(self.alpha[m].dot(xi))
                
            # Output layer
            ytmp = np.zeros(self.K)
            for k in range(self.K):
                ytmp[k] = G(U, self.beta, k)
                
            yp.append(ytmp)
                    
        return yp        

        
    def ForwardAndBackward(self, X, Y):
        """ Forward weight evaluation, Backward first derivative computations """
        n = len(X)
    
        yp = []    
        
        self.u = np.ones((n, self.M+1))

        self.delta = np.zeros((n, self.K))
        self.s = np.zeros((n, self.M))
            
        for i in range(n):
            xi = X[i]
            yi = [int(Y[i] == k) for k in range(10)]
            # Hidden layer
            for m in range(self.M):
                self.u[i,m] = Sigmoid(self.alpha[m].dot(xi))
                
            # Output layer
            ytmp = np.zeros(self.K)
            for k in range(self.K):
                ytmp[k] = G(self.u[i], self.beta, k)
                
            yp.append(ytmp)
            
            for k in range(self.K):
                self.delta[i,k] = -2*(yi[k]-ytmp[k])*DeG(self.u[i], self.beta, k)
                
            for m in range(self.M):
                self.s[i,m] = DevSigmoid(xi.dot(self.alpha[m]))
                tmp = 0
                for k in range(self.K):
                    tmp += self.beta[k,m]*self.delta[i,k]                
                self.s[i,m] = self.s[i,m]*tmp
        
        return yp
    
    def Learn(self, data):
        """ Learning algorithm with gradient descedent """
        
        xt, yt = ElaborateTrainingSet(data)    
    
        # Init
        yp = self.ForwardAndBackward(xt, yt)            
        loss = Loss(yp, yt)

        # Iterate a given number of times
        for it in range(100):
         
            yp = self.ForwardAndBackward(xt, yt)

            old_loss = loss            
            loss = Loss(yp, yt)
            if loss >= old_loss:
                # Decay for gamma "learning rate"
                self.gamma = self.gamma*0.9

            print(it, self.gamma, round(loss, 4))
            
            # Update weights
            for k in range(self.K):
                for m in range(self.M):
                    for i in range(len(xt)):
                        self.beta[k][m] -= self.gamma*(self.delta[i,k]*self.u[i,m])
        
            for m in range(self.M):
                for l in range(self.p):
                    for i in range(len(xt)):
                        self.alpha[m,l] -= self.gamma*self.s[i,m]*xt[i][l]
                

def TestANN(ann, x_test, y_test):
    """ Test the learned ANN on the given set of data """
    y_pred = ann.predict(x_test)
            
    print("Accuracy: ", accuracy_score(y_test, y_pred), ' - Number of itertions:', ann.n_iter_)
    
    # Write the predictinos in a .csv file
    with open('solution.csv','w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(['ImageId','Label'])
        for i,p in enumerate(y_pred):
            writer.writerow([i+1,p])


def EvaluateANN(ann, x_test):
    """ Test the learned ANN and produce output for Kaggle """
    start = time.time()
    
    y_pred = ann.predict(x_test)
    
    print('Evaluation time:', time.time()-start,'- size:', len(x_test))        
    print('Number of itertions:', ann.n_iter_)
    
    # Write the predictinos in a .csv file
    with open('solution.csv','w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(['ImageId','Label'])
        for i,p in enumerate(y_pred):
            writer.writerow([i+1,p])
    

#------------------------------------------
#              MAIN ENTRY POINT
#------------------------------------------
if __name__ == "__main__":
    # Misura il tempo per le operazioni principali
    start = time.time()
    
    # Fase 1: Training
    # Read CSV from Numpy, Link:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
    import iopro
    my_data = iopro.genfromtxt('Projects/MINST/train.csv', delimiter=',', skip_header=1)
    
    print('Reading time:', time.time()-start)
    
    start = time.time()
    
    ann = ANN(len(my_data[0]), 10, 10)
    
    ann.Learn(my_data)
    
    print('Learning time:', time.time()-start, '- size:', len(my_data))
    