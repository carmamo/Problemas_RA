#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:02:46 2019
Todos estos códigos requieren comentarios y una limpieza
Limpio=NO
Comentarios=NO
@author: carlos
"""

import control
import sympy 
import numpy
#from sympy import *  ##Importa todas las funciones de sympy para llamarlas directamente sin necesidad de usar sympy.()
#from control import * ##Importa todas las funciones de la libreria control para llamarlas sin necesidad de usar control.()
#from sympy import symbols ##Importa la funcion symbols de la libreria sympy para usarla sin necesidad de referenciarla usando sympy.()


s = sympy.Symbol('s')
k = sympy.Symbol('k', real=True)

G1 = 16/(s+(sympy.Rational(4,5)))
Ga = G1/(1+(G1*k))
G2 = 1/s
Gb = Ga*G2
M = Gb/(1+Gb)
#M = sym.simplify(M) ##simplifica pero no factoriza
M = sympy.factor(M)
#M = sym.powsimp(M)  ##simplificar con exponentes?

sympy.pprint(M)

"""
Calcular el valor de k
"""

Wn=numpy.sqrt(16)
z=0.5
k=(2*z*Wn-0.8)/16

print('')
print('')
print('k =', k)