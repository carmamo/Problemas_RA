#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:23:05 2019
Todos estos códigos requieren comentarios y una limpieza
Limpio=NO
Comentarios=NO
@author: carlos
"""
from numpy import *
from sympy import *
from control import *
from math import *


z=0.5
wn=4
wd=wn*sqrt(1-z**2)
theta=atan(sqrt(1-z**2)/z)


tr=(pi-theta)/wd
print('RiseTime:',format(tr, '.4f'))

tp=pi/wd
print('PeakTime:',format(tp, '.4f'))

Mp=exp(-z*pi/sqrt(1-z**2))
print('Overshoot:',format(Mp, '.4f'))

ts=4/(z*wn)
print('SettlingTime:',format(ts, '.4f'))
