from bitmap import *

def rellenando():
	rellenando = Bitmap(800,800)
	glViewPort(0,0,800,800)
	rellenando.load('./modelos/reyBooC2.obj', (500,200),(0.5,0.5))
	rellenando.archivo('out.bmp')

print(rellenando())