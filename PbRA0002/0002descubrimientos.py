#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:06:12 2019
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
t = np.arange(0.0, 15*ts, ts)
'''
proceso para pasar tfdata a num, den pero num, den aparece como una lista de numpy array
asi que hay que pasar de lista a numpy y luego usar flatten para 'aplanar' en un vector
esto sería equivalente al apartado c)
'''
(num, den)=ct.tfdata(Gz)
num=np.array(num) ##np.asarray hace lo mismo convierte tuple/list a array
den=np.array(den)
num=num.flatten()
den=den.flatten()
'''
pruebas con señales impulso, escalon y filtros low pass
'''
sys = signal.dlti(num, den) #dlti, no estoy seguro si es equivalente a muestrear el sistema,
                            #o si sirve para definir sistemas discretos usando (num, den)
t2, y = signal.dimpulse(sys, n=13)
y = np.array(y)
y = y.flatten()
plt.stem(t2, y, use_line_collection=True)
plt.margins(0.1, 0.1)  ##margenes
plt.xlabel('Time [sec]') ##label
plt.ylabel('Amplitude') ##label
plt.grid(True)
plt.show()

#low pass filter de la señal
response = signal.lfilter(num, den, t)
plt.plot(np.arange(0.0,15*ts, ts), response)  #np.arange es para dar valores al vector x
plt.margins(0.1, 0.1)  ##margenes
plt.xlabel('Time [sec]') ##label
plt.ylabel('Response') ##label
plt.grid(True) ##cuadricula
plt.show() ##equivalente a display/print
