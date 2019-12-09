#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:39:36 2019
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

'''
preparar numerador y denominador
'''
s = sym.symbols('s')
num=[1]
den= ( s*(s+1)*(s+5) )
## pon esto en la terminal para obtener coeficientes sym.Poly(den, s).all_coeffs()

G=ct.tf([1],[1, 6, 5, 0])
sys = ct.tf2ss(G)

print(sys)





#[numG,denG]=ct.tfdata(G, s)
#[A,B,C,D]=ct.tf2ss(numG,denG)