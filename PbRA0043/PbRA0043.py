#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:28:03 2020
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



t1=np.arange(0,2,0.01)
x1=np.zeros_like(t1)
t2=np.arange(2,4,0.01)
x2=1.5*(t2-2)/2
t3=np.arange(4,6,0.01)
x3=1.5*np.ones_like(t3)
t4=np.arange(6,10,0.01)
x4=1.5-1.5*(t4-6)/2
t5=np.arange(10,12,0.01)
x5=-1.5*np.ones_like(t5)
t6=np.arange(12,14,0.01)
x6=-1.5+1.5*(t6-12)/2
t7=np.arange(14,16,0.01)
x7=np.zeros_like(t7)

t = np.concatenate((t1,t2,t3,t4,t5,t6,t7))
x = np.concatenate((x1,x2,x3,x4,x5,x6,x7))



plt.plot(t,x)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Onda trapezoidal')