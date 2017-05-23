# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:01:34 2015

@author: Isaías Cuenca & Fran Navarro
@License: CC by 4.0 
Código original con ecuaciones diferenciales y explicación del modelo
tomado de Alex Sáez (Pybonacci.org)
http://pybonacci.org/2015/01/05/ecuaciones-de-lotka-volterra-modelo-presa-depredador/

"""

from __future__ import division
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import xlwings as xw


def main():
	wb = xw.Book.caller()

	def df_dt(x, t, a, b, c, d):
		"""Función del sistema en forma canónica"""
		dx = (a * x[0]-r*x[0]**2) - b * x[0] * x[1]
		dy = - c * x[1] + d * x[0] * x[1]
		return np.array([dx, dy])

	if xw.Range('W2').value.lower() == 'yes':
		animate = True; xw.App.ScreenUpdating = True
	else:
		animate = False; xw.App.ScreenUpdating = False

	# Parámetros (obtenidos de las casillas de excel)
	a = xw.Range('constante_a').value
	b = xw.Range('X4').value
	c = xw.Range('X5').value
	d = xw.Range('X6').value
	r = xw.Range('X7').value

	# Condiciones iniciales
	x0 = xw.Range('X13').value   # Presas
	y0 = xw.Range('X14').value    # Depredadores
	conds_iniciales = np.array([x0, y0])

	# Condiciones para integración
	tf = xw.Range('X10').value
	dt = xw.Range('X9').value
	N = int(tf/dt)
	t = np.linspace(0, tf, N)


	solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))


    # Escribiendo resultados en Excel
	if animate:
		for i in range(N):
			xw.Range((i+2,20)).value = t[i] # time
			xw.Range((i+2,21)).value = solucion[i, 0] # n presas
			xw.Range((i+2,22)).value = solucion[i, 1] # n deprededadores
	else:
		 xw.Range('T2').value = np.vstack(t)
		 xw.Range('U2').value = np.vstack(solucion[:, 0])
		 xw.Range('V2').value = np.vstack(solucion[:, 1])
         
	xw.App.ScreenUpdating = True
    
if __name__ == '__main__':
    if not hasattr(sys, 'frozen'):
        # The next two lines are here to run the example from Python
        # Ignore them when called in the frozen/standalone version
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'depredador.xlsm'))
        xw.Book.set_mock_caller(path)
    main()
