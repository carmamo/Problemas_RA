#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:30:41 2019
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


s, t = sym.symbols('s, t')
t = sym.symbols('t', positive=True) ##Si lo quitas aparece la función heaviside, positive implica real.
G=1/( s*(s+1)*(s+5) )
G=sym.inverse_laplace_transform(G, s, t)

sym.pprint(G)