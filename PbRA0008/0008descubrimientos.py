#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:11:20 2019
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
'''
función que cuadra matrices
'''
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
        

a = np.eye(5)*5       
a[0,1] = 230000000000
a[2,4] = 0.000005

matprint(a)

s = sym.symbols('s')
num=[1]
den= ( s*(s+1)*(s+5) )
den1 = sym.Poly(den)

denG1 = den1.all_coeffs()
print(denG1)

den2 = sym.expand(den)
denG2 = [den2.coeff(s**3),den2.coeff(s**2),den2.coeff(s),den2.coeff(0)]
print(denG2)
