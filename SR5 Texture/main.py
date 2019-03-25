from bitmap import *
from obj import *
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

def texturas():
	renderizando = Bitmap(1000,1000)
	glViewPort(0,0,800,800)

	t = Texture('./modelos/model.bmp')
	renderizando.renderer('./modelos/reyBoo.obj', scale=(0,0,0), translate=(0,0,0))
	#renderizando.texture('./modelos/face.obj',(800,800,0),(0.5,0.5,1), texture=t)
	renderizando.archivo('model.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(texturas())
