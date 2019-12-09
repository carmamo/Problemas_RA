#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:41:32 2019
Todos estos códigos requieren comentarios y una limpieza
Limpio=NO
Comentarios=NO
@author: carlos
"""
from control import *
from sympy import *
from numpy import *



Gp = tf(100,[1,0,100])
T = 0.05
Gz =sample_system(Gp, T)
pprint(Gz)


