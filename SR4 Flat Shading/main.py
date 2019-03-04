from bitmap import *

def rellenando():
	rellenando = Bitmap(800,800)
	glViewPort(0,0,800,800)
	rellenando.renderer('./modelos/test2.obj',(100,100,100),(4,3,3))
	rellenando.archivo('out.bmp')

print(rellenando())
