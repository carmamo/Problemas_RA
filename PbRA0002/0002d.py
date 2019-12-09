#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:49:43 2019
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



Gp = ct.tf(100,[1,0,100])
ts = 0.05
Gz =ct.sample_system(Gp, ts)
sym.pprint(Gz)
t = np.arange(0.0, 50*ts, ts)
(num, den)=ct.tfdata(Gp) ## por que GP???? lsim no funciona con Gz
num=np.array(num) ##np.asarray hace lo mismo convierte tuple/list a array
den=np.array(den)
num=num.flatten()
den=den.flatten()


do = ct.damp(Gz, doprint=True) ##damp me devuelve en vez de un vector, un tuple (parecido a una matriz) que contiene todos los datos
sys = signal.lti(num,den) ##transformo Gp en lti que es lo que acepta la syntax de lsim
wn=do[0] ## 0 contiene wn, 1 contiene damping, 2 contiene eigen de los dos polos

x=np.sin(wn[0]*t) ##escojo el valor de wn de un polo

fig, ax=plt.subplots()

tout, a, b = signal.lsim(sys, x, t)
plt.plot(t, x)
plt.step(t, a)
plt.show()