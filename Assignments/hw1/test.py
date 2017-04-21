# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:37:40 2017

@author: gualandi

Funzione di test per il primo homework.
Da eseguire all'interno dell'ambiente Spyder o da linea di comando:
    
    > python test.py
 
NOTA: il file test.py e compito_2.py da testare devono essere nella stessa directory 
"""



#------------------------------------------
#              MAIN ENTRY POINT
#------------------------------------------
if __name__ == "__main__":
    
    from compito_2 import *
    
    print(NomeCognome())
    
    print('Test 1:', And([True, True, False, True]) == False)
    print('Test 2:', And([True, True, True, True]) == True)
    
    print('Test 3:', Or([True, True, False, True]) == True)
    print('Test 4:', Or([False, False, False, False]) == False)
    
    print('Test 5:', Length(list(range(13))) == 13)
    
    print('Test 6:', Reverse([3,4,1,2]) == list(reversed([3,4,1,2])))
    print('Test 7:', Reverse(list(range(13))) == list(reversed(range(13))))
    
    from math import factorial
    print('Test 8:', FoldFactorial(7) == factorial(7))

    print('Test 9:', SumLength([3,4,1,2]) == (10,4))
    
    print('Test 10:', Map(lambda x: x**2, list(range(5))) == [x**2 for x in range(5)])
    
    print('Test 11:', Filter(lambda x: x%2 == 0, list(range(10))) == [0,2,4,6,8])

    print('Test 12:', FoldLeft(lambda x,y: 1+y, 0, list(range(10))) == 10)
    
    primi = NumeriPrimi()
    print('Test 13:', [next(primi) for _ in range(10)] == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23])

    fib = Fibonacci()
    print('Test 14:', [next(fib) for _ in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34])
    