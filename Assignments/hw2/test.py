# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:08:27 2017

@author: gualandi
"""

import pandas as pd
import csv

from sklearn.metrics import accuracy_score

#------------------------------------------
#              MAIN ENTRY POINT
#------------------------------------------
if __name__ == "__main__":
    
    from compito_131313 import *
   
    print(NomeCognome())
    
    df = pd.read_csv('train.csv')
        
    P = Train(df)
    
    dt = pd.read_csv('test.csv')
    y_pred = P(dt)
    
    with open('solution.csv','w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        writer.writerow(['PassengerId','Survived'])
        for i,p in zip(dt['PassengerId'], y_pred):
            writer.writerow([i,p])