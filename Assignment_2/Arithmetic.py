''' This Module is set of fucnctions Containing Arit'''

def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Mult(a,b):
    return a*b

def Div(a,b):
    return  a/b

#Assignment 3 
def fact(a):        
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

#Assignment 4 for Factor addition
def factorAdd(a):
    fact=0
    for i in range(1,9) :
        if (a % i == 0 ):
            fact=fact+i
    return fact

#Assignment 5
def Prime(a):
    for i in range(2,a) :
        if ( a % i == 0 ):
            return False
            break
        else :
            return True