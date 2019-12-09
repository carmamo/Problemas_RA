#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:23:05 2019
Todos estos códigos requieren comentarios y una limpieza
Limpio=NO
Comentarios=NO
@author: carlos
"""
import math as m
import control as ct

"""
solo funciona con funciones de transferencia de segundo orden
"""
def step_info(sysc):
    
    wn, damping, poles = ct.damp(sysc, doprint=False)
    z=damping[0]
    wn=wn[0]
    wd=wn*m.sqrt(1-(z)**2)
    theta=m.atan(m.sqrt(1-(z)**2)/(z))


    tr=(m.pi-theta)/wd
    print('RiseTime:',format(tr, '.4f'))

    ts=4/((z)*(wn))
    print('SettlingTime:',format(ts, '.4f'))
    
    Mp=(m.exp(-z*m.pi/m.sqrt(1-(z)**2)))*100
    print('Overshoot:',format(Mp, '.4f'),'%')
    
    tp=m.pi/wd
    print('PeakTime:',format(tp, '.4f'))
    print('')
    print('')
    
    return

#Gp2 = ct.tf([80],[5, 20, 80])
#step_info(Gp2)
#Gp4 = ct.tf([1, 5, 5],[1, 1.65, 5, 6.5, 2])
#step_info(Gp4)

Q1 = 5
G = ct.tf([1],[5,1,0])
G1=Q1*G
G1c=ct.feedback(G1,1)


Q2 = 5*(ct.tf([0.8,1],[1]))
G2 = Q2*G
G2c = ct.feedback(G2,1)
print(G2c)


G3a = ct.tf([5],[5,1])
G3b = ct.feedback(G3a,0.8)
G3d = G3b*ct.tf([1],[1,0])
G3c = ct.feedback(G3d,1)
print(G3d)


step_info(G1c)
step_info(G2c)
step_info(G3c)