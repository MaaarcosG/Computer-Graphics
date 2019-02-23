from bmp import *

# Cargamos el archivo donde se guardar
filename('personaje_nes.bmp')
glCreateWindow(200,200)
glViewPort(10,10,32,32)
glClearColor(0,0,0)
glClear()
glColor(1,0,0)
#------ Creacion de Lineas -----#
glLine(50,150,30,30)
glLine(50,150,31,31)
#------ Creacion de Cuerpo IZQUIERDO -----#
glLine(40,50,33,33)
glLine(40,50,34,34)
i = 1
y1 = 34
y2 = 34
while (i<26):
	glLine(40,37,(y1+i),(y2+i))
	i+=1
#------ Cuerpo abajo de caparazon IZQUIERDO-----#
glLine(40,25,60,60)
glLine(40,25,61,61)

i = 1
y1 = 60
y2 = 60
while (i<19):
	glLine(25,26,(y1+i),(y2+i))
	i+=1

glLine(10,40,81,81)
glLine(10,40,82,82)

i = 1
y1 = 82
y2 = 82
while (i<10):
	glLine(37,40,(y1+i),(y2+i))
	i+=1

#------ Linea divisora entre caparazon -----#

glLine(40,150,94,94)
glLine(40,150,95,95)

#------ Creacion de Cuerpo DERECHO -----#

glLine(150,160,33,33)
glLine(150,160,34,34)

i = 1
y1 = 32
y2 = 32
while (i<28):
	glLine(157,160,(y1+i),(y2+i))
	i+=1


#------ Cuerpo abajo de caparazon DERECHO-----#

glLine(157,172,60,60)
glLine(157,172,61,61)

i = 1
y1 = 60
y2 = 60
while (i<19):
	glLine(172,169,(y1+i),(y2+i))
	i+=1

glLine(150,180,81,81)
glLine(150,180,82,82)

i = 1
y1 = 82
y2 = 82
while (i<10):
	glLine(150,153,(y1+i),(y2+i))
	i+=1

#------ OJOS DEL HONGITO IZQUIERDO ------#

i = 1
y1 = 91
y2 = 91
while (i<20):
	glLine(70,79,(y1-i),(y2-i))
	i+=1
#------ OJOS DEL HONGITO DERECHO ------#

i = 1
y1 = 91
y2 = 91
while (i<20):
	glLine(111,120,(y1-i),(y2-i))
	i+=1
#------ CAPARAZON LADO IZQUIERDO ------#	

i = 1
y1 = 80
y2 = 80 
while (i<65):
	glLine(10,15,(y1+i),(y2+i))
	i+=1

i = 1
y1 = 144
y2 = 144
while (i<5):
	glLine(10,30,(y1+i),(y2+i))
	i += 1

i = 1
y1 = 148
y2 = 148
while (i<20):
	glLine(25,30, (y1+i),(y2+i))
	i +=1

glLine(25,40,168,168)
glLine(25,40,169,169)
glLine(25,40,170,170)

i = 1
y1 = 170
y2 = 170
while (i<8):
	glLine(35,40,(y1+i),(y2+i))
	i += 1

glLine(40,47,178,178)
glLine(40,47,179,179)
glLine(40,47,180,180)
glLine(40,47,181,181)

i = 1
y1 = 181
y2 = 181
while (i<5):
	glLine(46,56,(y1+i),(y2+i))
	i += 1

#-------Linea del Tope -----#

glLine(55,138,187,187)
glLine(55,138,188,188)
glLine(55,138,189,189)

#------ CAPARAZON LADO DERECHO -----#
i = 1
y1 = 80
y2 = 80 
while (i<65):
	glLine(180,175,(y1+i),(y2+i))
	i+=1
	
i = 1
y1 = 144
y2 = 144
while (i<5):
	glLine(180,165,(y1+i),(y2+i))
	i += 1

i = 1
y1 = 148
y2 = 148
while (i<20):
	glLine(170,165, (y1+i),(y2+i))
	i +=1

glLine(155,170,168,168)
glLine(155,170,169,169)
glLine(155,170,170,170)

i = 1
y1 = 170
y2 = 170
while (i<8):
	glLine(155,160,(y1+i),(y2+i))
	i += 1

glLine(147,154,178,178)
glLine(147,154,179,179)
glLine(147,154,180,180)
glLine(147,154,181,181)

i = 1
y1 = 181
y2 = 181
while (i<5):
	glLine(140,147,(y1+i),(y2+i))
	i += 1

#----- HONGO EN MEDIO DE LA CABEZA -----#




glFinish()