#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:48:51 2020
Todos estos códigos requieren comentarios y una limpieza
Limpio=NO
Comentarios=NO
@author: carlos
"""
import control as ct
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.ticker import (MultipleLocator)



T=1 #Longitud de semiperiodo
t=[]
x=[]
 
for i in [0,1,2,3]:
    ti = i*2 #  Comienzo de un periodo
    t1 = np.linspace(ti,ti+T,100)
    x1 = np.zeros(100)
    if i<3:
        t2 = np.linspace(ti+T,ti+2*T,100) # Devuelve array con comienzo en ti+T y fin en ti+2T (1 a 2, 3 a 4, 5 a 6,..)
        x2 = t2-(ti+T) # Hacemos que el incremento de x2 sea de 0 a 1, restando a t2, ti+T (comienzo de semiperiodo) que es el instante inicial de la pendiente
    else:
        t2 = np.linspace(6,7,100) 
        x2 = np.zeros(100) 
        
    t = np.concatenate((t,t1,t2))
    x = np.concatenate((x,x1,x2))



plt.plot(t,x)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Diente de sierra')