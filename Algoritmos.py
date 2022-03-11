import numpy as np
import math
from Ctes import P,n,A,MIN_INTERES,MAX_INTERES,BISECCION_CORTE,CONVERGENCIA_CORTE

def f(x): 
    return (P/x)*((pow(1+x,n)-1)) - A

def biseccion(a,b,f): 
  
    if (f(a) * f(b) >= 0): 
        print("Los valores del intervalo no cumplen la hipótesis del teorema\n") 
        return
   
    return biseccion_(a,b,f)
    
def biseccion_(a,b,f):   

    m = ((a+b)/2) 

    if(abs((a-b)) < BISECCION_CORTE): 
        return m

    if (f(m)*f(a) < 0): 
        return biseccion_(a,m,f) 
    else: 
        return biseccion_(m,b,f)   

def g1(x):
    return x - (((P/x)*((pow(1+x,n)-1))) - A)
def g2(x):
    return pow((A*x/P)+1,1/n) - 1
def g3(x):
    return (P/A) * (pow(1+x,n) - 1)
def g4(x):
    return pow((((A*x/P)+1)/pow(1+x,n/2)),2/n) - 1
def g5(x):
    return x - (((P/x)*(pow(1+x,n)-1))-A) / (((-P/pow(x,2))*((1+pow(x,n))-1)) + ((P/x)* n * (pow(1+x,n-1))))

def imprimirER(Xo,X1):
    return str(abs((X1-Xo)/Xo))

def imprimirVA(Xo,X1):
    return str(Xo)

def verificarConvergencia(g,Xo,imp = False, f = False):
    while True:
        X1 = np.float32(Xo)
        Xo = np.float32(g(X1))
        if(math.isnan(abs((X1-Xo/Xo)))):
            return False
        if f != False and imp != False:
            f.write(imp(Xo,X1))
            f.write(',')    
        if(abs((X1-Xo)/Xo) < CONVERGENCIA_CORTE):
            return True
        if(Xo < MIN_INTERES or Xo > MAX_INTERES):
            return False

def encontrarIDC(verif,g,Xinf,Xsup,rango):
    a = Xinf
    b = Xsup
    while verif(g,Xsup) == False:
        Xsup -= rango
        if Xsup <= a:
           print('El algoritmo no converge en el intervalo(',a,',',b,')')
           return

    print('El supremo del I.D.C es',Xsup)

    while verif(g,Xinf) == False:
        Xinf += rango
        if Xinf >= b:
           print('El algoritmo no converge en el intervalo(',a,',',b,')')
           return

    print('El infimo del I.D.C es',Xinf)            