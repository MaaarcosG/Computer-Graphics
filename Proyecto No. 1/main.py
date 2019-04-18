# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

from bmp import *

objetos = Bitmap(1000,1000)

#RENDERIZADO DE LOS PERSONAJES CON LAS PISTOALAS (FUNCIONANDO)

#Renderizado personaje de la izquierda
objetos.lookAt(V3(-1,0,5), V3(0.8,0.7,0), V3(0,1,0))
objetos.load('./models/p1.obj', mtl='./models/p1.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -4, 0))

#Renderizado del personaje de la derecha
objetos.lookAt(V3(1,0,5), V3(-0.8,0.7,0), V3(0,1,0))
objetos.load('./models/p2.obj', mtl='./models/p2.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -1, 0))

#RENDERIZADO A LOS PERSONAJES QUE CONTIENEN LOS SABLES DE LUZ (FUNCIONANDO)

#Personaje de la derecha
objetos.lookAt(V3(1,1,5), V3(-0.4,0,0), V3(0,1,0))
objetos.load('./models/p3.obj', mtl='./models/p3.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -1, 0))

#Personaje de la izquierda
objetos.lookAt(V3(1,1,5), V3(-0.8,0,0), V3(0,1,0))
objetos.load('./models/p3.obj', mtl='./models/p3.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -0.1, 0))

#El darkvader en medio de todos
objetos.lookAt(V3(1,1,5), V3(-0.3,-0.3,0), V3(0,1,0))
objetos.load('./models/vader.obj', mtl='./models/vader.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -0.3, 0), texture=None)


# TOQUE DE LA CASA
# En el siguiente codigo se renderizara a goku, UNICAMENTE PARA FINES DE CALIDAD
#Codigo para renderizar a goku
goku = Texture('./models/goku.bmp')
objetos.lookAt(V3(-1,0,5), V3(0.8,-0.65,0), V3(0,1,0))
objetos.load('./models/goku.obj', mtl=None, translate=(0,0,0), scale=(0.5,0.5,0.5), rotate=(0,1,0), texture=goku)

#Importamos la funcion donde se imprimira todo
objetos.archivo('ESCENA_FINAL.bmp')
