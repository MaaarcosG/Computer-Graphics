from bmp import *

def reyBoo():
	filename('reyBoo.bmp')
	glCreateWindow(800,800)
	glViewPort(10,10,32,32)
	glClearColor(0,0,0)
	glClear() 
	glColor(1,1,1)
	#utilizamos la funcion lineas
	load('./modelos/eje.obj', (3,4),(10,40))
	glFinish()

print(reyBoo())