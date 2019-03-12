from bitmap import *
from obj import *
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

def texturas():
	renderizando = Bitmap(1000,1000)
	glViewPort(0,0,800,800)

	t = Texture('./models/model.bmp')

	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	#renderizando.renderer('./models/model.obj', (200,200,200),(3,3,3))
	renderizando.texture('./models/model.obj',(1, 1, 1), (300, 300, 300), texture=t)
	renderizando.archivo('tierra.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(texturas())
5
