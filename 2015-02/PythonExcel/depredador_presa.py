# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:01:34 2015

@author: Isaías Cuenca
@License: CC by 4.0 
Código original con ecuaciones diferenciales
tomado de Alex Sáez (Pybonacci.org)
http://pybonacci.org/2015/01/05/ecuaciones-de-lotka-volterra-modelo-presa-depredador/

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from xlwings import Workbook, Range, Chart

wb = Workbook.caller()

def df_dt(x, t, a, b, c, d):
    """Función del sistema en forma canónica"""
    dx = (a * x[0]-r*x[0]**2) - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    return np.array([dx, dy])

if Range('W2').value.lower() == 'yes':
    animate = True
else:
    animate = False

# Parámetros
a = Range('constante_a').value
b = Range('X4').value
c = Range('X5').value
d = Range('X6').value
r = Range('X7').value

# Condiciones iniciales
x0 = Range('X13').value   # Presas
y0 = Range('X14').value    # Depredadores
conds_iniciales = np.array([x0, y0])

# Condiciones para integración
tf = Range('X10').value
N = 50
N = Range('X9').value
N = int(N)
t = np.linspace(0, tf, N)


solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))
#representaciones graficas
#plt.plot(t, solucion[:, 0], label='presa')
#plt.plot(t, solucion[:, 1], label='depredador')



nn = np.linspace(0, N, N)
if animate:
    for i in range(1,N):
        #nn[i] = i
        #Range('D1').value = np.vstack(nn)
        Range((i+1,20)).value = t[i-1]
        Range((i+1,21)).value = solucion[i-1, 0]
        Range((i+1,22)).value = solucion[i-1, 1]
        wb.xl_app.Application.ScreenUpdating = True
else:
     Range('T2').value = np.vstack(t)
     Range('U2').value = np.vstack(solucion[:, 0])
     Range('V2').value = np.vstack(solucion[:, 1])

