#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:44:16 2020
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



t1=np.arange(0,10,0.01)
x1=np.zeros_like(t1)
t2=np.arange(10,30,0.01)
x2=10*(t2-10)/20
t3=np.arange(30,50,0.01)
x3=10*np.ones_like(t3)
t4=np.arange(50,80,0.01)
x4=-0.5*np.ones_like(t4)
t5=np.arange(80,100,0.01)
x5=2*np.ones_like(t5)


t = np.concatenate((t1,t2,t3,t4,t5))
x = np.concatenate((x1,x2,x3,x4,x5))

fig, ax = plt.subplots()
ax.plot(t,x)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(2))
plt.margins(0.05, 0.05)

plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Onda trapezoidal')