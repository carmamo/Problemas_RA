#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:54:51 2019
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




Q1 = 5
G = ct.tf([1],[5,1,0])
G1=Q1*G
G1c=ct.feedback(G1,1)
sym.pprint(G1c)

Q2 = 5*(ct.tf([0.8,1],[1]))
G2 = Q2*G
G2c = ct.feedback(G2,1)
sym.pprint(G2c) 

G3a = ct.tf([5],[5,1])
G3b = ct.feedback(G3a,0.8)
G3d = G3b*ct.tf([1],[1,0])
G3c = ct.feedback(G3d,1)
sym.pprint(G3c)
 
t = np.arange(0.0,20.0,0.01)
T, y1i = ct.impulse_response(G1c,t)
T, y2i = ct.impulse_response(G2c,t)
T, y3i = ct.impulse_response(G3c,t)
plt.figure(1).show()
plt.title('Respuesta al impulso')
plt.plot(t, y1i, t, y2i, t, y3i)

 

T, y1e = ct.step_response(G1c,t)
T, y2e = ct.step_response(G2c,t)
T, y3e = ct.step_response(G3c,t)
plt.figure(2).show()
plt.title('Respuesta al escalón')
plt.plot(t, y1e, t, y2e, t, y3e)


x = t
(num1, den1)=ct.tfdata(G1c)
num1 = np.array(num1).flatten()
den1 = np.array(den1).flatten()
(num2, den2)=ct.tfdata(G2c)
num2 = np.array(num2).flatten()
den2 = np.array(den2).flatten()
(num3, den3)=ct.tfdata(G3c)
num3 = np.array(num3).flatten()
den3 = np.array(den3).flatten()
tout, y1r, b = signal.lsim((num1,den1),x,t)
tout, y2r, b = signal.lsim((num2,den2),x,t)
tout, y3r, b = signal.lsim((num3,den3),x,t)
plt.figure(3).show()
plt.title('Respuesta lineal')
plt.plot(x, y1r, x, y2r, x, y3r)

"""
No existe un equivalente a stepinfo() en python, habria que calcular usando las formulas.
No debe ser difícil implementar una función que haga lo mismo que stepinfo pero por ahora
no tengo los conocimientos como para esto
"""
