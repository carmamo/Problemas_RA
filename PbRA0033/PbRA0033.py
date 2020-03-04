#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:13:48 2020
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


t1=np.arange(-2,0,0.01)
t2=np.arange(0,10,0.01)
t=np.concatenate((t1,t2))

# Constantes del sistema
Ks=1
tau=1
Q0=1 
 
Q=Q0*np.concatenate((np.zeros_like(t1),np.ones_like(t2))) # Entrada escalón
 
C = (Q/Ks)*(1-np.exp(-t/tau)) # Salida

plt.plot(t,Q,'r',t,C)
plt.xlabel('Tiempo')
plt.ylabel('Concentración')