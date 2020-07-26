"""
Universidad del Valle de Guatemala
Cifrado de Informacion
Seccion 10
Lic. Luis Alberto Suriano
Grupo 4

main.py
Proposito: Crear una linea dentro del framebuffer con las posibles optimizaciones
"""
#Imnportar pylfsr en pip install
import numpy as np
from pylfsr import LFSR

L = LFSR()

# print the info
L.info()
L.runKCycle(10)
L.info()
L.runFullCycle()
L.info()