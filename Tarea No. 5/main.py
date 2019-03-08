from bitmap import *
from obj import Mtl
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909


def reyBoo():
	renderizando = Bitmap(600,600)
	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	colores = Mtl('./modelos/ReyBoo.mtl')
	renderizando.renderer('./modelos/ReyBoo.obj',(100,100,100),(3,3,3))
	colores.kd

	for materiales in colores.kd:
		c = len(materiales)

	print(c)
	renderizando.archivo('output.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(reyBoo())
