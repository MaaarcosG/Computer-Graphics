# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909
# Fecha: 08 de febrero del 2019

import struct
import math
from obj import *

def char(c):
	return struct.pack("=c",c.encode('ascii'))

def word(c):
	return struct.pack("=h",c)

def dword(c):
	return struct.pack("=l",c)

def color(r,g,b):
	return bytes([b,g,r])

#Variables globales
windows = None
filename = "out.bmp"
ViewPort_X = None
ViewPort_Y = None
ViewPort_H = None
ViewPort_W = None


def filename(name):
	global filename
	filename = name

#Funcion que inicializara el escritorio de imagen
def glCreateWindow(width,height):
	global windows
	#Declar la clase con relacion a una variable global
	windows = Bitmap(width, height)

#Funcion definara el area de la imagen
def glViewPort(x,y,width,height):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W
	#variable View Port en el eje x
	ViewPort_X = x
	#variable View Port en el eje y
	ViewPort_Y = y

	#variable View Port del ancho de la imagen
	ViewPort_H = height
	#variable View Port de la altura
	ViewPort_W = width

#Funcion que limpiara
def glClear():
	global windows
	#Llamo la funcion clear que se encuentra en la clase bitmap
	windows.clear()

#Funcion que limpiara el color
def glClearColor(r,g,b):
	global windows
	#windows.clear(int(255*r),int(255*g),int(255*b))

	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño
	R = int(math.floor(r * 255))
	G = int(math.floor(g * 255))
	B = int(math.floor(b * 255))
	#Devuelve los numeros para crear otro color, es decir limpiar el color. 
	print("Limpieza de color: %d, %d, %d" % (R,G,B))
	windows.clearColor = color(R,G,B)


#Funcion que cambie el color de un punto.
def glVertex(x,y):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows
	
	PortX = int((x+1) * ViewPort_W * (1/2) + ViewPort_X)
	PortY = int((y+1) * ViewPort_H * (1/2) + ViewPort_Y)
	print('glVertex X: %d y %d' % (PortX,PortY))
	windows.point(PortX,PortY)

#Funcion para cambiar el color de la funcion glVertex
def glColor(r,g,b):
	global windows
	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño
	R = int(math.floor(r * 255))
	G = int(math.floor(g * 255))
	B = int(math.floor(b * 255))
	#Devuelve los numeros para crear otro color, es decir limpiar el color. 
	print("Vertex Color: %d, %d, %d" % (R,G,B))
	windows.vertexColor = color(R,G,B)

#Funcion para crear lineas
def glLine(x1,x2,y1,y2):
	global windows
	#--------# y = mx + b #--------# 
	#Valores en X
	dx = abs(x2-x1)
	#Valores en Y
	dy = abs(y2-y1)

	#Condicion cuando la pendiente es ---> (dy/0)
	if dx == 0:
		for y in range(y1, y2+1):
			windows.point(x1, y)
		return 0

	#Condicion para completar la linea
	if(dy>dx):
		x1,y1 = y1,x1
		x2,y2 = y2,x2
	
	if(x1>x2):
		x1,x2 = x2,x1
		y1,y2 = y2,y1

	llenar = 0
	limite = 0
	x = x1
	y = y1
	
	#pendiente
	#m = dy/dx
	for x in range(x,(x2+1)):
		if (dy>dx):
			windows.point(y,x)
		else:
			windows.point(x,y)
		llenar += dy * 2
		if llenar >= limite:
			y += 1 if y1 < y2 else -1
			limite += 2*dx

#Funcion para terminar
def glFinish():
	global windows
	windows.write(filename)

def load(filename, translate=(0,0), scale=(1,1)):
	#cargamos el archivo
	global windows
	objeto = Obj(filename)
	
	#Ciclo para recorer las caras
	for face in objeto.faces: 
		#Conteo de los vertices
		vcount = len(face)
		#print(vcount)
		for vertice in range(vcount):
			#coordenada = (x,y)
			listCoor = []
			x1 = round((objeto.vertices[vertice-1][0]+translate[0]*scale[0]))
			x2 = round((objeto.vertices[vertice-1][1]+translate[1]*scale[1]))
			y1 = round((objeto.vertices[vertice-1][0]+translate[0]*scale[0]))
			y2 = round((objeto.vertices[vertice-1][1]+translate[1]*scale[1]))

			listCoor.append(x1)
			listCoor.append(x2)
			listCoor.append(y1)
			listCoor.append(y2)

			glLine(x1,x2,y1,y2)		

			#f1 = face[j][0]
			#f2 = face[(j+1)%vcount][0]
			
			#v1 = objeto.vertices[f1-1]
			#v2 = objeto.vertices[f2-1]
			
			#-------------- GENERALIZANDO --------------#
			#x1 = round(v1[0] + translate[0] * scale[0])
			#x2 = round(v2[1] + translate[1] * scale[1])
			#y1 = round(v1[0] + translate[0] * scale[0])
			#y2 = round(v2[1] + translate[1] * scale[1])

			#glLine(x1,x2,y1,y2)
			
#CLASE QUE GENERA ESCRITORIO DE IMAGEN
class Bitmap(object):
	#constructor de la clase
	def __init__(self, width,height):
		self.width = width
		self.height = height
		self.framebuffer = []
		self.clearColor = color(91,204,57)
		self.vertexColor = color(0,0,0)
		self.clear()

	def clear(self):
		self.framebuffer = [
		[
			self.clearColor
				for x  in range(self.width)
			]
   			for y in range(self.height)

		]
	def write(self,filename="out.bmp"):
		f = open(filename,'bw')
		#file header (14)
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(14 + 40))

		#image header (40)
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])
		f.close()

	#def point(self, x, y):
		#self.framebuffer[y][x]= self.vertexColor

	def point(self, x, y, color = None):
		try:
			self.framebuffer[y][x] = color or self.vertexColor
		except:
			pass

