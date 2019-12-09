#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:02:46 2019

@author: carlos
"""

import control
import sympy as sym
from sympy import symbols
#import numpy


s,k = symbols('s,k', commutative= True)



sys1 = control.TransferFunction(16, [1,0.8])
print(sys1)
H = (k)
sysa = control.feedback(sys1, k)
sys2 = control.TransferFunction(1, [1,0])
sysb = control.series(sysa, sys2)
M = control.feedback(sysb, 1)

print(M)
