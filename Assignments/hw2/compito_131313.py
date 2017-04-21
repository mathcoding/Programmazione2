# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:59:25 2017

@author: gualandi
"""

def NomeCognome():
    return "Kunta Kid 131313"

def sex2int(x):
    """ Converti sesso"""
    try:
        return int(x=='male')
    except:
        return -1

def Train(Xs):
    def ConvertInput(data):
        data['Sex'] = data['Sex'].apply(sex2int)
        return data
    
    def FilterInput(data):
        data = data[data['Sex'] >= 0]
        return data
        
    def Predict(x_test):
        x_test = ConvertInput(x_test)
        
        # Se avete fatto un fitting qui dovete richiamare il 
        # metodo per fare le previsioni
        y_pred = [sex for sex in x_test['Sex']]
        
        return y_pred

    # Parte principale della funzione 'Train'
    
    # Elabora i dati
    Xs = ConvertInput(Xs)
    Xs = FilterInput(Xs)
    
    # Fitting dei dati con il vostro metodo scelto

    # Esempio insignificanti: sopravvivono solo i maschi
    # NO FITTING                
    
    return Predict