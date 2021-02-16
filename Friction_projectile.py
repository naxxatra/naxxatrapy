# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:56:48 2021

@author: Lenovo
"""

from sympy import *
def friction(mu_s,mu_k,m,g,theta):
    if theta!=0:
       N=m*g*sin(theta)
    elif theta==0:
         N=m*g
       
    force_static=mu_s*N
    force_kinetic=mu_k*N
    return force_static
    return force_kinetic
    pass
def projectile(theta1,g,u,x):
    y=sin(theta1)*x/cos(theta1)-(g/(2*u**2*cos(theta1)**2))*x**2
    t_a=u*sin(theta1)/g
    t_fl=2*u*sin(theta1)/g
    h_max=u**2*(sin(theta1))**2/2*g
    r=u**2*sin(2*theta1)/g
    if theta1==45:
       r=(u**2)/g
       
    return y
    return t_a
    return t_fl
    return h_max
    return r
    pass
