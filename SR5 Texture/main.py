from bitmap import *
from obj import *
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

def texturas():
	renderizando = Bitmap(800,800)
	glViewPort(0,0,800,800)

	t = Texture('./modelos/goku.bmp')
	#renderizando.load('./modelos/goku.obj', scale=(0,0,0), translate=(0,0,0), texture=t)
	renderizando.load('./modelos/goku.obj', translate=(1,1,1), scale=(350,350,350), texture=t)
	#renderizando.texture('./modelos/face.obj',(800,800,0),(0.5,0.5,1), texture=t)
	renderizando.archivo('texture.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(texturas())
