import math
def an(a,q,n):
    return a*pow(q,n-1)

def ank(ak,q,n,k):
    return ak*pow(q,n-k)

def suma0(a,q,n):
    return a*((1-pow(q,n))/(1-q))

def suma1(a,n):
    return a*n

def czygeo(x,y,z):
    if y**2==x*z:
        print("Tworzą ciąg geometryczny")
    else:
        print("Nie tworzą ciąg geometryczny")