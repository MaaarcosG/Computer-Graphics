# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

# importamos la libreria necesaria para las Funciones
from bmp import *
import random
import algebra as op

objetos = Bitmap(1000,1000)
objetos.glCreateWindow(1000,1000)
objetos.glViewPort(0,0,999,999)

def shaders(barycentricas=(1,1,1), vnormals=0, bcolor=(1,1,1)):
    # base del color para el modelo
	bcolor = (255,233,0)
    # coordenadas barycentricas
	w, v, u = bary
    # coordenadas para el vector normal
	nA, nB, nC = Vnormals
    # luz del modeli
	light = (0,0,1)
    # calculamos cada uno de los
	iA = sr.dot(nA, light)
	iB = sr.dot(nB, nA)
	iC = sr.dot(nC, nB)

	intensity = w*iA + v*iB + u*iC

	if intensity <= 0:
		intensity = 0.85
	elif intensity < 0.25:
		intensity = 0.75
	elif intensity < 0.75:
		intensity = 0.55
	elif intensity < 1:
		baseColor = (1,1,0)
		intensity = 0.80


	r = intensity * baseColor[0]
	g = intensity * baseColor[1]
	b = intensity * baseColor[2]

''' debug
puebra = op.dot(2,2)
print(puebra)
'''
objetos.lookAt(V3(-1,0,5), V3(0.8,-0.8,0), V3(0,1,0))
objetos.load('./models/sol.obj', mtl='./models/sol.mtl', translate=(0,0,0), scale=(0.2,0.2,0.2), rotate=(0,1,0), shader=None)
