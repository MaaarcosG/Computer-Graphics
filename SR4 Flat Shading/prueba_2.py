from bitmap import *

def rellenando():
	r = Bitmap(800,800)
	glViewPort(0,0,800,800)
	r.load('./modelos/Test2.obj', (500,200),(0.5,0.5))
	r.display('out.bmp')

print(rellenando())
