# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

from bmp import *
import random
import algebra

objetos = Bitmap(800,800)
objetos.glCreateWindow(800,800)
objetos.glViewPort(0,0,999,999)

# TOQUE DE LA CASA
# En el siguiente codigo se renderizara a goku
#Codigo para renderizar a goku
goku = Texture('./modelos/goku.bmp')
objetos.lookAt(V3(1,0,5), V3(-0.3,-0.3,0), V3(0,1,0))
objetos.load('./modelos/goku.obj', mtl=None, translate=(0,0,0), scale=(1,1,1), rotate=(0,1,0), texture=goku)

#Importamos la funcion donde se imprimira todo
objetos.archivo('Goku.bmp')
