from bitmap import *

# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

'''
Por fines de puebra por alguna razon con el modelo de ReyBoo.mtl y ReyBoo.obj los colores no se añaden
por lo cual para pobrar el codigo se utilizo otro modelo
'''
def batman():
	renderizando = Bitmap(600,600)
	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	renderizando.renderer_color('./modelos/p3.obj', mtl='./modelos/p3.mtl', scale=(100,100,100), translate=(3,3,3))
	renderizando.archivo('output.bmp')

def lego():
	renderizando = Bitmap(600,600)
	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	renderizando.renderer_color('./modelos/p3.obj', mtl='./modelos/p3.mtl', scale=(100,100,100), translate=(3,3,3))
	renderizando.archivo('lego.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(lego())
