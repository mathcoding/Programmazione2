def NomeCognome():
	return "Paolo Rossi 423023"

## PARTE PRIMA: ESERCIZI CON FOLD
##-------------------------------

def FoldR(F, v, Ls):
    if Ls == []:
        return v
    else:
        return F(Ls[0], FoldR(F,v,Ls[1:]))
        
def And(Ls):
    def MyAnd(x,y):
        return x and y
    return FoldR(MyAnd, True, Ls)

def Or(Ls):
    def MyOr(x,y):
        return x or y
    return FoldR(MyOr, False, Ls)

def Length(Ls):
    return FoldR(lambda x,y: 1+y, 0, Ls)

def Reverse(Ls):
    def Concatenate(x, Ls):
        return Ls + [x]
    return FoldR(Concatenate, [], Ls)

def FoldFactorial(n):
    return FoldR(lambda x,y: x*y, 1, [i+1 for i in range(n)])
    
def SumLength(Ls):
    return FoldR(lambda x,y: (x+y[0], 1+y[1]), (0,0), Ls)
    
def Map(F, Ls):
    return FoldR(lambda x,y: [F(x)]+y, [], Ls)

def Filter(F, Ls):
    return FoldR(lambda x,y: [x] + y if F(x) else y, [], Ls)

def FoldLeft(F, v, Ls):
    if Ls == []:
        return v
    else:
        return FoldLeft(F,F(v,Ls[0]),Ls[1:])


## PARTE SECONDA: LISTA INFINITA NUMERI PRIMI
##-------------------------------------------

def NumeriPrimi():
    yield 1
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

def Fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b