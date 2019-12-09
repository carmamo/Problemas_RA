#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:47:43 2019
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



s = sym.symbols('s')
num=[1]
den= ( s*(s+1)*(s+5) )
## pon esto en la terminal para obtener coeficientes sym.Poly(den, s).all_coeffs()

G = ct.tf([1],[1, 6, 5, 0])

Gz = ct.sample_system(G,0.2) #zoh zero order hold es el predeterminado, retenedor de orden cero

print(Gz) ## si pones Gz directamente en el terminal, sale más 'bonito'