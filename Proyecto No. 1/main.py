# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

from bmp import *
import random

objetos = Bitmap(1000,1000)
objetos.glCreateWindow(1000,1000)
objetos.glViewPort(0,0,999,999)


#Codigo para hacer efecto de gravedad
objetos.glLine(10,10,10,110)
objetos.glLine(990,10,10,10)
objetos.glLine(990,110,10,110)
objetos.glLine(990,10,990,110)

#Lineas para hacer efecto de gravedad
i = 10
x1 = 20
x2 = 20
while(i<950):
    objetos.glLine((x1+i),20,(x2+i),50)
    i += 1

#Lineas que hacen el efecto de gravedad
objetos.glLine(90, 70, 90, 100)
objetos.glLine(150, 70, 150, 100)
objetos.glLine(210, 70, 210, 100)
objetos.glLine(270, 70, 270, 100)
objetos.glLine(330, 70, 330, 100)
objetos.glLine(390, 70, 390, 100)
objetos.glLine(450, 70, 450, 100)
objetos.glLine(510, 70, 510, 100)
objetos.glLine(570, 70, 570, 100)
objetos.glLine(630, 70, 630, 100)
objetos.glLine(690, 70, 690, 100)
objetos.glLine(750, 70, 750, 100)
objetos.glLine(810, 70, 810, 100)
objetos.glLine(870, 70, 870, 100)
objetos.glLine(930, 70, 930, 100)
objetos.glLine(990, 70, 990, 100)

#Codigo que genera la bala del laser
objetos.glColor(1,0,0)
objetos.glLine(310,310,750,310)

#Codigo para lluvia de estrellas
for x in range(random.randint(1,1000)):
    X = random.uniform(-1,1)
    Y = random.uniform(-1,1)
    objetos.glColor(1,1,0)
    objetos.glVertex(X,Y)

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
objetos.load('./models/p4.obj', mtl='./models/p4.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -0.1, 0))

#El darkvader en medio de todos
objetos.lookAt(V3(1,1,5), V3(-0.3,-0.3,0), V3(0,1,0))
objetos.load('./models/vader.obj', mtl='./models/vader.mtl', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -0.3, 0))


#Efecto del sol
objetos.lookAt(V3(-1,0,5), V3(0.8,-0.8,0), V3(0,1,0))
objetos.load('./models/sol.obj', mtl='./models/sol.mtl', translate=(0,0,0), scale=(0.2,0.2,0.2), rotate=(0,1,0))

'''
# TOQUE DE LA CASA
# En el siguiente codigo se renderizara a goku, UNICAMENTE PARA FINES DE PRUEBA
#Codigo para renderizar a goku
goku = Texture('./models/goku.bmp')
objetos.lookAt(V3(-1,0,5), V3(0.8,-0.65,0), V3(0,1,0))
objetos.load('./models/goku.obj', mtl=None, translate=(0,0,0), scale=(1,1,1), rotate=(0,1,0), texture=goku)
'''

#Importamos la funcion donde se imprimira todo
objetos.archivo('EscenaFinal.bmp')
