from bmp import *

def reyBoo():
	filename('reyBoo.bmp')
	glCreateWindow(800,800)
	glViewPort(0,0,800,800)
	#utilizamos la funcion lineas
	load('./modelos/test2.obj', (500,200),(0.6,0.6))
	glFinish()

print(reyBoo())