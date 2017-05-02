# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:43:05 2017

@author: gualandi
"""
import time

import numpy as np
from numpy import genfromtxt

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def DrawDigit(A, label=''):
    """ Draw single digit as a greyscale matrix"""
    fig = plt.figure(figsize=(6,6))
    # Uso la colormap 'gray' per avere la schacchiera in bianco&nero
    img = plt.imshow(A, cmap='gray_r')
    plt.xlabel(label)
    plt.show()
    
def ElaborateInput(data):
    """ Prepare input data """
    X = []
    Y = []    
    for row in data:
        X.append(np.array(row[1:]))
        Y.append(int(row[0]))        
    return X, Y

def LearnANN(data):
    """ Learn an Artificial Neural Network and return the corresponding object """
    x_train, y_train = ElaborateInput(data)    
    
    # PRIMA DI FARE QUESTO ESERCIZIO, STUDIARE IL TUTORIAL:
    # http://scikit-learn.org/stable/modules/neural_networks_supervised.html
    #
    # ESERCIZIO DA FARE: PROVARE I DIVERSI PARAMETRI DI QUESTA CLASSE
    # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    ann = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    ann.fit(x_train, y_train)
    return ann

def TestANN(ann, x_test, y_test):
    """ Test the learned ANN on the given set of data """
    y_pred = ann.predict(x_test)
            
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    

#------------------------------------------
#              MAIN ENTRY POINT
#------------------------------------------
if __name__ == "__main__":
    # Misura il tempo per le operazioni principali
    start = time.time()
    
    # Fase 1: Training
    # Read CSV from Numpy, Link:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
    my_data = genfromtxt('Projects/MINST/train.csv', delimiter=',', skip_header=1)            
    print('Reading time:', time.time()-start)
    start = time.time()

    # Cambia in True per plottare alcune immagine
    if False:
        for row in my_data[:9]:
            # Documentation for function 'reshape':
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
            A = np.array(row[1:]).reshape(28,28)        
            DrawDigit(A, 'Digit: ' + str(int(row[0])))

    ann = LearnANN(my_data)
    
    print('Learning time:', time.time()-start, '- size:', len(my_data))
    start = time.time()
    
    # Fase 2: Evaluate    
    my_test = genfromtxt('Projects/MINST/test.csv', delimiter=',', skip_header=1)
    x_test, y_test = ElaborateInput(my_test)
    
    TestANN(ann, x_test, y_test)
    print('Evaluation time:', time.time()-start,'- size:', len(my_test))

