from bmp import *

def prueba():
	filename('prueba.bmp')
	glCreateWindow(800,800)
	glViewPort(0,0,800,800)
	#utilizamos la funcion lineas
	load_2('./modelos/Test2.obj', (500,200),(0.5,0.5))
	glFinish()

print(prueba())