# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:43:05 2017
"""


import time
import csv
import numpy as np

from numpy import genfromtxt
from matplotlib import plt

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def DrawDigit(A, label=''):
    """ Draw single digit as a greyscale matrix"""
    fig = plt.figure(figsize=(6,6))
    # Uso la colormap 'gray' per avere la schacchiera in bianco&nero
    img = plt.imshow(A, cmap='gray_r')
    plt.xlabel(label)
    plt.show()

    
def ElaborateTrainingSet(data):
    """ Elaborate training set """
    X = []
    Y = []    
    for row in data:
        X.append(np.array(row[1:]))
        Y.append(int(row[0]))        
    return X, Y


def ElaborateTestSet(data):
    """ Elaborate test set """
    X = []
    for row in data:
        X.append(np.array(row))

    return X

def LearnANN(data):
    """ Learn an Artificial Neural Network and return the corresponding object """
    x_train, y_train = ElaborateTrainingSet(data)    
    
    # PRIMA DI FARE QUESTO ESERCIZIO, STUDIARE IL TUTORIAL:
    # http://scikit-learn.org/stable/modules/neural_networks_supervised.html
    #
    # DA COMPLETARE: PROVARE I DIVERSI PARAMETRI DI QUESTA CLASSE
    # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    ann = MLPClassifier(hidden_layer_sizes=(1), random_state=1)
    # COME VOLETE PROGETTARE LA VOSTRA RETE MULTILIVELLO???
    
    ann.fit(x_train, y_train)
    
    # ESERCIZIO 2: INVECE DI USRARE LA LIBRERIA SCIKIT, IMPLEMENTARE UNA RETE
    #              NEURALE BASANDOSI SULL'ESEMPIO VISTO AL SEMINARIO DEL 4 maggio 2017
    return ann


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
    
    print('Evaluation time:', time.time()-start,'- size:', len(my_test))        
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
    
    # Fase 2: local test for learning of parameters
    # DA COMPLETARE TORVARE I VOSTRI PARAMETRI NEL MODO CHE PREFERITE
    
    # Fase 3: Evaluate on Kaggle test set
    my_test = genfromtxt('Projects/MINST/test.csv', delimiter=',', skip_header=1)
    x_test = ElaborateTestSet(my_test)    
    EvaluateANN(ann, x_test)