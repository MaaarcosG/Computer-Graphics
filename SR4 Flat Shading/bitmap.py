# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

import struct
import math
from obj import *
#Importamos la coleccion
from collections import namedtuple

#Variables globales
ViewPort_X = None
ViewPort_Y = None
ViewPort_H = None
ViewPort_W = None

v2 = namedtuple('Punto2', ['x', 'y'])
v3 = namedtuple('Punto3', ['x', 'y', 'z'])


def char(c):
	return struct.pack("=c",c.encode('ascii'))

def word(c):
	return struct.pack("=h",c)

def dword(c):
	return struct.pack("=l",c)

def color(r,g,b):
	return bytes([b,g,r])

#------ FUNCIONES PARA TRABJAR CON VECTORES DE LONGITUD 3 ------#

#Suma de vectores
def resta(v0,v1):
	#Puntos en cada coordenadas
	px = v0.x + v1.x
	py = v0.y + v1.y
	pz = v0.z + v1.z

	#retorna un vector nuevo con la suma
	return v3(px,py,pz)

#Resta de coordeadas
def resta(v0,v1):
	#Puntos en cada coordenadas
	px = v0.x - v1.x
	py = v0.y - v1.y
	pz = v0.z - v1.z

	#retorna un vector nuevo con la resta
	return v3(px,py,pz)

def mul(v0,k):
	#Puntos en cada coordenadas
	px = v0.x * k
	py = v0.y * k
	pz = v0.z * k

	#retorna un vector nuevo con la multiplicacion a un escalar
	return v3(px,py,pz)

def dot(v0,v1):
	return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

#Funcion que encontrar un vector nuevo, utlizando algebra producto cruz
def pCruz(v0,v1):
	#Puntos en cada coordenadas
	p1 = v0.y * v1.z - v0.z * v1.y
	p2 = v0.z * v1.x - v0.x * v1.z
	p3 = v0.x * v1.y - v0.y * v1.x

	#Retorna un nuevo vector
	return v3(p1,p2,p3)

#Funcion para la longitud del vector
def longitud(v0):
	px = v0.x
	py = v0.y
	pz = v0.z
	#Suma de puntos
	len = px+py+pz
	return len

#Funcion para encontrar el vector normal
def normal(v0):
	v0Lon = longitud(v0)

	if not v0Lon:
		return v3(0,0,0)

	px = v0.x/v0Lon
	py = v0.y/v0Lon
	pz = v0.z/v0Lon

	return v3(px,py,pz)

#Bounding Box
def bbox(*vertices):
	xs = [vertex.x for vertex in vertices]
	xy = [vertex.y for vertex in vertices]
	xs.sort()
	ys.sort()

	p1 = xs[0], ys[0]
	p2 = xs[-1], ys[-1]
	return v2(p1), v2(p2)

#Funcion para encontrar las coordenadas barycentricas
def baricentricas(A,B,C,P):
	bcoor = pCruz((v3(C.x - A.x, B.x - A.x, A.x - P.x)),(v3(C.y - A.y, B.y - A.y, A.y - P.y)))

	if abs(bcoor[2] < 1):
		return(-1,-1,-1)

	return (1 - (bcoor[0] + bcoor[1]) / bcoor[2], bcoor[1] / bcoor[2], bcoor[0] / bcoor[2])

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

#Transformar datos a normal
def nor(n):
	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows
	nx = int(ViewPort_H * (n[0]+1) * (1/2) + ViewPort_X)
	ny = int(ViewPort_H * (n[1]+1) * (1/2) + ViewPort_Y)
	return nx, ny

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

	def archivo(self, filename='out.bmp'):
		self.write(filename)

	def point(self, x, y):
		self.framebuffer[y][x]= self.vertexColor

	def glLine(self, vertex1, vertex2):
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
				self.point(x1, y)
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
				self.point(y,x)
			else:
				self.point(x,y)
			llenar += dy * 2
			if llenar >= limite:
				y += 1 if y1 < y2 else -1
				limite += 2*dx

	def load(self, filename, scale=(1, 1), translate=(0, 0)):
		objeto = Obj(filename)
		for face in objeto.faces:
			vcount = len(face)
			for j in range(vcount):
				#Por cada cara se saca modulo para emparejamiento.
				i = (j+1)%vcount
				f1 = face[j][0]
				f2 = face[i][0]
				v1 = objeto.vertices[f1 - 1]
				v2 = objeto.vertices[f2 - 1]
				#Le damos un valor a las coordeadas
				x1 = round((v1[0] + translate[0]) * scale[0]);
				y1 = round((v1[1] + translate[1]) * scale[1]);
				x2 = round((v2[0] + translate[0]) * scale[0]);
				y2 = round((v2[1] + translate[1]) * scale[1]);
				#Guardando las coordenadas en un lista
				vertex = []
				vertex.append(x1)
				vertex.append(y1)
				vertex.append(x2)
				vertex.append(y2)
				self.glLine((vertex[0],vertex[1]),(vertex[2],vertex[3]))

	def triangulos(self,A,B,C, color=None):
		b_min, b_max = bbox(A,B,C)

		for x in range(b_min.x, b_max.x+1):
			for y in range(b_min.y, b_max.y):
				w, v, u = baricentricas(A,B,C, v2(x,y))
				if  w < 0 or v < 0 or u < 0:
					continue
				z = A.z * w + B.z * v + C.z * u

				if z > self.zbuffer[x][y]:
					self.point(x,y,color)
					self.zbuffer[x][y] = z

	#Vector 3 transformado
	def transform(self, vertex, translate=(0, 0, 0), scale=(1, 1, 1)):
		p_x = round((vertex[0] + translate[0]) * scale[0])
		p_y = round((vertex[1] + translate[1]) * scale[1])
		p_z = round((vertex[2] + translate[2]) * scale[2])

		return v3(p_x, p_y, p_z)

	#Funcion para el zbuffer
	def renderer(self, filename, scale=(1, 1), translate=(0, 0)):
		objeto = Obj(filename)
		#uz = v3(0,0,1)
		for face in objeto.faces:
			nvectores = len(face)


			if nvectores == 3:
				f1 = face[0][0] - 1
				f2 = face[1][0] - 1
				f3 = face[2][0] - 1

				a = self.transform(objeto.vertices[f1],scale,translate)
				b = self.transform(objeto.vertices[f2],scale,translate)
				c = self.transform(objeto.vertices[f3],scale,translate)

				#Luz
				#luz = v3(0,0,1)
				vector_normal = normal(pCruz(resta(b,a),resta(c,a)))
				intensidad = dot(vector_normal,v3(0,0,1))
				tono = round(255 * intensidad)
				if tono<0:
					continue

				self.triangulos(a,b,c, color(tono,tono,tono))

			else:
				f1 = face[0][0] - 1
				f2 = face[1][0] - 1
				f3 = face[2][0] - 1
				f4 = face[3][0] - 1

				#Lista para cada vertices
				list_vertice = []
				v1 = self.transform(objeto.vertices[f1],scale,translate)
				v2 = self.transform(objeto.vertices[f2],scale,translate)
				v3 = self.transform(objeto.vertices[f3],scale,translate)
				v4 = self.transform(objeto.vertices[f4],scale,translate)
				#Añadimos las coordeadas
				list_vertice.append(v1)
				list_vertice.append(v2)
				list_vertice.append(v3)
				list_vertice.append(v4)

				vector_normal = normal(pCruz(resta(list_vertice[0],list_vertice[1]),resta(list_vertice[1],list_vertice[2])))
				intensidad = dot(vector_normal,v3(0,0,1))
				tono = round(255 * intensidad)
				if tono<0:
					continue

				A,B,C,D = list_vertice

				self.triangulos(A,B,C, color(tono,tono,tono))
				self.triangulos(A,C,D, color(tono,tono,tono))


	#Rellenando cualquier poligono funciones utilizadas para el laboratorio No. 1
	def filling_any_polygon(self,vertices):
		#global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows
		#numero de vertices
		nvertices = len(vertices)

		#Calculando los Y maximos y minimos
		ymax = sorted(vertices, key=lambda tup: tup[1], reverse=True)[0][1]
		ymin = sorted(vertices, key=lambda tup: tup[1])[0][1]
		#Calculamos los X maximo y minimos
		xmin = sorted(vertices, key=lambda tup: tup[0])[0][0]
		xmax = sorted(vertices, key=lambda tup: tup[0], reverse=True)[0][0]

		#Lista de coordenadas
		self.glLine(vertices[0], vertices[-1])

		#Ciclo para encontrar el numero de vertices de un poligono
		for i in range(nvertices-1):
			if i  != nvertices:
				self.glLine(vertices[i], vertices[i+1])

		for x in range(xmin, xmax):
			for y in range(ymin, ymax):
				dentro = self.verificar_puntos(x,y,vertices)
				if dentro:
					self.point(x,y)

	#Verificando cada uno de los puntos dentro de los poligonos funciones utilizadas para el laboratorio No. 1
	def verificar_puntos(self,x,y,vertices):
		#Algoritmo obtenido de: http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
		counter = 0
		p1 = vertices[0]
		n = len(vertices)
		for i in range(n+1):
			p2 = vertices[i % n]
			if(y > min(p1[1], p2[1])):
				if(y <= max(p1[1], p2[1])):
					if(p1[1] != p2[1]):
						intersecciones_x = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
						if(p1[0] == p2[0] or x <= intersecciones_x):
							counter += 1
			p1 = p2
		if(counter % 2 == 0):
			return False
		else:
			return True
