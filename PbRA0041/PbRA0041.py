#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:34:00 2020
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


t1=np.arange(0,5,0.01)
x1=np.zeros_like(t1)
t2=np.arange(5,10,0.01)
x2=np.ones_like(t2)
t3=np.arange(10,15,0.01)
x3=np.zeros_like(t3)
t4=np.arange(15,20,0.01)
x4=-np.ones_like(t4)
t5=np.arange(20,25,0.01)
x5=np.zeros_like(t5)

t=np.concatenate([t1,t2,t3,t4,t5])
x=np.concatenate([x1,x2,x3,x4,x5])
 
fig, ax = plt.subplots()
ax.plot(t,x)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
plt.margins(0.01, 0.25)

plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Onda cuadrada')



"""
'otra opcion'

t1=np.arange(0,5,0.01)
t2=np.arange(5,10,0.01)
t3=np.arange(10,15,0.01)
t4=np.arange(15,20,0.01)
t5=np.arange(20,25,0.01)

ceros=np.zeros((500,1))
unos=np.ones((500,1))
menosunos=-np.ones((500,1))

t=np.array([t1,t2,t3,t4,t5]).flatten()
x=np.array([ceros,unos,ceros,menosunos,ceros]).flatten()

fig, ax = plt.subplots()
ax.plot(t,x)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
plt.margins(0.01, 0.25)
"""

'''
x = np.arange(0,30,5)
y = np.array((0,1,0,-1,0,0))

plt.step(x, y, where='post', label='escalon')
plt.plot(x, y, 'C2o', alpha=0.5)

plt.legend(title='Onda cuadrada')
plt.show()
'''


ceros=np.zeros((500,1))
unos=np.ones((500,1))
menosunos=-np.ones((500,1))

t=np.arange(0,25,0.01).flatten()
'x=np.stack([ceros,unos,ceros,menosunos,ceros], axis=0).flatten()'
x=np.concatenate([ceros,unos,ceros,menosunos,ceros])

fig, ax1 = plt.subplots()
ax1.plot(t,x)
ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(0.5))
plt.margins(0.01, 0.25)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Onda cuadrada')