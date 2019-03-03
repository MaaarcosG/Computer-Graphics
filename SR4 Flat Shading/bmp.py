# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909
# Fecha: 08 de febrero del 2019

import struct
import math
from obj import *
#Importamos la coleccion
from collections import namedtuple

#Creamos los vectores
v2 = namedtuple('Point2', ['x','y'])
v3 = namedtuple('Point3', ['x','y','z'])

#Variables globales
windows = None
filename = "out.bmp"
ViewPort_X = None
ViewPort_Y = None
ViewPort_H = None
ViewPort_W = None


def char(c):
	return struct.pack("=c",c.encode('ascii'))

def word(c):
	return struct.pack("=h",c)

def dword(c):
	return struct.pack("=l",c)

def color(r,g,b):
	return bytes([b,g,r])

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
	#print("Limpieza de color: %d, %d, %d" % (R,G,B))
	windows.clearColor = color(R,G,B)


#Funcion que cambie el color de un punto.
def glVertex(x,y):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	PortX = int((x+1) * ViewPort_W * (1/2) + ViewPort_X)
	PortY = int((y+1) * ViewPort_H * (1/2) + ViewPort_Y)
	#print('glVertex X: %d y %d' % (PortX,PortY))
	windows.point(PortX,PortY)

#Funcion para cambiar el color de la funcion glVertex
def glColor(r,g,b):
	global windows
	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño
	R = int(math.floor(r * 255))
	G = int(math.floor(g * 255))
	B = int(math.floor(b * 255))
	#Devuelve los numeros para crear otro color, es decir limpiar el color.
	#print("Vertex Color: %d, %d, %d" % (R,G,B))
	windows.vertexColor = color(R,G,B)

#Funcion para terminar
def glFinish():
	global windows
	windows.write(filename)

#Funcion para calcular el producto cruz
def pCruz(v0,v1):
	vector_1 = v0.y * v1.z - v0.z * v1.y
	vector_2 = v0.z * v1.x - v0.x * v1.z
	vector_3 = v0.x * v1.y - v0.y * v1.x

	v3 = (vector_1,vector_2,vector_3)

	return v3

#Funcion para calcular el producto punto
def pPunto(v0,v1):
	vec = ((v0.x * v1.x) + (v0.y * v1.y) + (v0.z * v1.z))
	return vec

#Longitud del vector
def longitud(v0):
	length = (v0.x + v0.y + v0.z)
	return length

#Funcion para encontrar el vector normal
def normal(v0):
	lon = longitud(v0)
	if not lon:
		return v3(0,0,0)

	return v3(v0.x/lon, v0.y/lon, v0.z/lon)

#Resta de la colección
def rest(v0,v1):
	resta = v3((v0.x - v1.x), (v0.y - v1.y), (v0.z - v1.z))
	return resta

def box(*vertice):
	xs = [vertex.x for vertex in vertice]
	ys = [vertex.y for vertex in vertice]
	xs.sort()
	ys.sort()

	return v2(xs[0],ys[0]), v2(xs[-1],ys[-1])

#Funcion para crear lineas
def glLine(vertex1, vertex2):
	global windows

	x1 = vertex1[0]
	y1 = vertex1[1]
	x2 = vertex2[0]
	y2 = vertex2[1]
	#--------# y = mx + b #--------#
	#Valores en X
	dx = abs(x2-x1)
	#Valores en Y
	dy = abs(y2-y1)
	st = dy > dx
	#Condicion cuando la pendiente es ---> (dy/0)
	if dx == 0:
		for y in range(y1, y2+1):
			windows.point(x1, y)
		return 0
	#Condicion para completar la linea
	if(st):
		x1,y1 = y1,x1
		x2,y2 = y2,x2
	if(x1>x2):
		x1,x2 = x2,x1
		y1,y2 = y2,y1
	#Valores en X
	dx = abs(x2-x1)
	#Valores en Y
	dy = abs(y2-y1)
	llenar = 0
	limite = dx
	y = y1
	#pendiente
	#m = dy/dx
	for x in range(x1,(x2+1)):
		if (st):
			windows.point(y,x)
		else:
			windows.point(x,y)
		llenar += dy * 2
		if llenar >= limite:
			y += 1 if y1 < y2 else -1
			limite += 2*dx

def load(filename, translate=(0,0), scale=(1,1)):
	#Abrimos el archivo
	objeto = Obj(filename)

	for cara in objeto.faces:
		#Lista para guardar cada uno de los vertices
		verticesCaras = []
		for vertice in cara:
			coordenadaVertice = nor(objeto.vertices[vertice-1])
			#Vertices en x
			vx = int((coordenadaVertice[0] + translate[0]) * scale[0])
			#Vertices en y
			vy = int((coordenadaVertice[1] + translate[1]) * scale[1])
			coordenadaVertice = (vx,vy)
			#Agragamos los vertices a la lista
			verticesCaras.append(coordenadaVertice)

		#numero de vertices dentro de la lista
		nvertices = len(verticesCaras)
		#La primera linea utlizando los vertices correctoss
		glLine(verticesCaras[0], verticesCaras[-1])

		#Ciclo para encontrar las uniones de cada uno de las caras
		for i in range(nvertices-1):
			if i  != nvertices:
				glLine(verticesCaras[i], verticesCaras[i+1])

		filling_any_polygon(verticesCaras)

def filling_any_polygon(vertices):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows
	#numero de vertices
	nvertices = len(vertices)

	#Calculando los Y maximos y minimos
	ymax = sorted(vertices, key=lambda tup: tup[1], reverse=True)[0][1]
	ymin = sorted(vertices, key=lambda tup: tup[1])[0][1]
	#Calculamos los X maximo y minimos
	xmin = sorted(vertices, key=lambda tup: tup[0])[0][0]
	xmax = sorted(vertices, key=lambda tup: tup[0], reverse=True)[0][0]

	#Lista de coordenadas
	glLine(vertices[0], vertices[-1])

	#Ciclo para encontrar el numero de vertices de un poligono
	for i in range(nvertices-1):
		if i  != nvertices:
			glLine(vertices[i], vertices[i+1])

	for x in range(xmin, xmax):
		for y in range(ymin, ymax):
			dentro = verificar_puntos(x,y,vertices)
			if dentro:
				windows.point(x,y)

def verificar_puntos(x,y,vertices):
	#Algoritmo obtenido de: http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
	counter = 0
	p1 = vertices[0]
	n = len(vertices)
	for i in range(n+1):
		p2 = vertices[i % n]
		if(y > min(p1[1], p2[1])):
			if(y <= max(p1[1], p2[1])):
				if(p1[1] != p2[1]):
					xinters = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
					if(p1[0] == p2[0] or x <= xinters):
						counter += 1
		p1 = p2
	if(counter % 2 == 0):
		return False
	else:
		return True

#Coordenadas barycentricas
def barycentric(A,B,C,P):
	BARY = pCruz(v3(C.x - A.x, B.x - A.x, A.x - P.x), v3(C.y - A.y, B.y - A.y, A.y - P.y))

	if abs(BARY[2] < 1):
		return -1,-1,-1

	return (1 - (bary[0] + bary[1]) / bary[2], bary[1] / bary[2], bary[0] / bary[2])

def triangle(self, A,B,C, color=None):
	bmin, bmax = box(A,B,C)
	for x in range(bmin.x,bmax.x+1):
		for y in range(bmin.y,bmax.y+1):
			w,v,y = barycentric(A,B,C, v2(x,y))

		if (w<0) or (v<0) or (u<0):
			continue

		z = A.z * w + B.z * v + C.z * u

		if z > zbuffer[x][y]:
			windows.point(x,y,color)
			zbuffer[x][y] = z

#Transformamos el vector
def transform(vertex,translate=(0,0,0),scale=(1,1,1,)):
	ver_1 = round((vertex[0] + translate[0]) * scale[0])
	ver_2 = round((vertex[1] + translate[1]) * scale[1])
	ver_3 = round((vertex[2] + translate[2]) * scale[2])

	return v3(ver_1,ver_2,ver_3)

#Transformar datos a normal
def nor(n):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows
	return int(ViewPort_H * (n[0]+1) * (1/2) + ViewPort_X), int(ViewPort_H * (n[1]+1) * (1/2) + ViewPort_X)

class Vertex(object):
	def __init__(self, vert):
		self.x = vert[0]
		self.y = vert[1]

	def __str__(self):
		return "x: " + str(self.x) + " y: " + str(self.y)

Negro = color(0,0,0)
Blanco = color(255,255,255)
#CLASE QUE GENERA ESCRITORIO DE IMAGEN
class Bitmap(object):
	#constructor de la clase
	def __init__(self, width,height):
		self.width = width
		self.height = height
		self.framebuffer = []
		self.clearColor = Blanco
		self.vertexColor = Blanco
		self.clear()

	def clear(self):
		self.framebuffer = [[Negro for x  in range(self.width)] for y in range(self.height)]
		self.zbuffer = [[-float('inf') for x in range(self.width)] for y in range(self.height)]

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
