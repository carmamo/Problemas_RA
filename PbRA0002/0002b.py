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

"""
apartado b)
"""
polos = ct.pole(Gz)
magnitudpolos = abs(polos)
sym.pprint(magnitudpolos)
