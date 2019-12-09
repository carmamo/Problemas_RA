#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:57:34 2019
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


"""
apartado c.1)
"""

#t = np.arange(0.0, 15*ts, ts)   ## equivalente a t=0:T*14:T
t = np.linspace(0,14*ts,num=15)

#imp = signal.unit_impulse(15, 4)  ##impulso unitario
T, yout = ct.impulse_response(Gz, t)
yout=yout.flatten()
#plot(np.arange(0.0,15*ts, ts), imp)   ##Descomentar para ver la señal impulso unitario
fig, ax = plt.subplots()
ax.step(T, yout)
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
plt.margins(0.1, 0.1)  ##margenes
plt.title('Impulse Response c.1)')
plt.xlabel('Time [sec]') ##label
plt.ylabel('Amplitude') ##label
plt.grid(True) ##cuadricula
plt.show() ##equivalente a display/print


"""
apartado c.2)
"""

plt.stem(T, yout, use_line_collection=True)
plt.margins(0.1, 0.1)  ##margenes
plt.title('Impulse Response c.2)')
plt.xlabel('Time [sec]') ##label
plt.ylabel('Amplitude') ##label
plt.grid(True) ##cuadricula
plt.show() ##equivalente a display/print



