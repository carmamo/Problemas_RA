#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:03:09 2019
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
ct.use_matlab_defaults()

"""
para graficas interactivas hay que meter en la terminal el comando %matplotlib auto
para graficas "inline" %matplotlib inline
"""


G=ct.tf([2],[1,2,0,2])

rlist, klist = ct.root_locus(G, grid=True)

plt.show()

