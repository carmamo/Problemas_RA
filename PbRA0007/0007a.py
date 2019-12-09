#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:30:38 2019
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
ct.use_matlab_defaults()


K=2 #Valor inicial
a=2 #Valor inicial
'''
primero pasamos las funciones de transferencia usando matematicas simbolicas
para asi obtener el vector del numerador y denominador
'''

s = sym.symbols('s')

Q=sym.expand(K*(s+a)**2)/s
G=1.2/sym.expand((0.3*s+1)*(s+1)*(1.2*s+1))

sym.pprint(Q)
sym.pprint(G)
#ct.sisotool(G,Q)

'''
pasamos a tf y usamos sisotools
'''

Q = ct.tf([K, 2*K*a, K*(a**2)],[1,0])
G = ct.tf([1.2],[0.36,1.86,2.5,1])


#ct.sisotool(Q)  ##Error all the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 1 and the array at index 2 has size 2
ct.sisotool(G) ##vuelve a dar problemas kvect a la hora de concordar con matlab, no comprendo el uso del vector