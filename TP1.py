import numpy as np
import math
import Algoritmos as Alg
from Ctes import P,n,A,BISECCION_A,BISECCION_B,MAX_INTERES,MIN_INTERES,IDC_RANGO
np.seterr(invalid='ignore')

msgFile = open('mensaje.txt','rt') 
print(msgFile.read())
outputFile = open ('output.txt','wt')

root = Alg.biseccion(np.float64(BISECCION_A),np.float64(BISECCION_B),Alg.f)
print('El valor de la raiz es:', root)

while True:
    Xs = np.float32(input('Ingrese un valor para la semilla:\n'))
    if(Xs <= MIN_INTERES or Xs >= MAX_INTERES):
        print('El valor ingresado es inválido')
    else:
        break

print('')

outputFile.write('Algoritmo 1:\n')
if Alg.verificarConvergencia(Alg.g1,Xs,Alg.imprimirER,outputFile) == True :
    print('El Algoritmo 1 es convergente para esta semilla')
else :        
    print('El Algoritmo 1 no es convergente para esta semilla')
outputFile.write('\n')

outputFile.write('Algoritmo 2:\n')
if Alg.verificarConvergencia(Alg.g2,Xs,Alg.imprimirER,outputFile) == True:
    print('El Algoritmo 2 es convergente para esta semilla')
else:        
    print('El Algoritmo 2 no es convergente para esta semilla')
outputFile.write('\n')

outputFile.write('Algoritmo 3:\n')
if Alg.verificarConvergencia(Alg.g3,Xs,Alg.imprimirER,outputFile) == True :
    print('El Algoritmo 3 es convergente para esta semilla')
else:        
    print('El Algoritmo 3 no es convergente para esta semilla')
outputFile.write('\n')

outputFile.write('Algoritmo 4:\n')
if Alg.verificarConvergencia(Alg.g4,Xs,Alg.imprimirER,outputFile) == True :
    print('El Algoritmo 4 es convergente para esta semilla')
else:        
    print('El Algoritmo 4 no es convergente para esta semilla')
outputFile.write('\n')

outputFile.write('Algoritmo 5:\n')
if Alg.verificarConvergencia(Alg.g5,Xs,Alg.imprimirER,outputFile) == True :
    print('El Algoritmo 5 es convergente para esta semilla')
else:        
    print('El Algoritmo 5 no es convergente para esta semilla')    
outputFile.write('\n')

print('\nDeterminación de Intervalos de Convergencia:')

print('Algoritmo 1:')
Alg.encontrarIDC(Alg.verificarConvergencia,Alg.g1,MIN_INTERES + IDC_RANGO,MAX_INTERES - IDC_RANGO,IDC_RANGO)            
print('Algoritmo 2:')
Alg.encontrarIDC(Alg.verificarConvergencia,Alg.g2,MIN_INTERES + IDC_RANGO,MAX_INTERES - IDC_RANGO,IDC_RANGO)            
print('Algoritmo 3:')
Alg.encontrarIDC(Alg.verificarConvergencia,Alg.g3,MIN_INTERES + IDC_RANGO,MAX_INTERES - IDC_RANGO,IDC_RANGO)            
print('Algoritmo 4:')
Alg.encontrarIDC(Alg.verificarConvergencia,Alg.g4,MIN_INTERES + IDC_RANGO,MAX_INTERES - IDC_RANGO,IDC_RANGO)            
print('Algoritmo 5:')
Alg.encontrarIDC(Alg.verificarConvergencia,Alg.g5,MIN_INTERES + IDC_RANGO,MAX_INTERES - IDC_RANGO,IDC_RANGO)            
