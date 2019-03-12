# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.faces = []
        self.read()

    def read(self):
        for lineas in self.lines:
            if lineas:
                prefix, value = lineas.split(' ', 1)
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])

#Clase que abre y guarda dentro de una lista los valores de kd
class Mtl(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.ka = []
        self.kd = []
        self.ke = []
        self.materiales =[]
        self.read()

    def read(self):
        for lineas in self.lines:
            if lineas:
                prefix, valor = lineas.split(' ', 1)
                if prefix == 'Kd' :
                    self.kd.append(list(map(float, valor.split(' '))))

                if prefix == 'newmtl':
                    self.nombre.append(list(valor.split(' ')))



"""
from bitmap import *
POR MOTIVO DE RENDERIZACION EL CODIGO PARA ABRIR EL OBJ LO TUVE QUE CAMIBAR Y UTILIZAR EL EJEMPLO DE LA CLASE
class Obj(object):
	def __init__(self,filename):
		#with open(filename) as f:
			#self.lines = f.read().splitlines()

		self.filename = filename
		self.vertices = []
		self.faces = []
		self.read()

	def read(self):
		#Abrimos el archivo
		archivo = open(self.filename, 'r')

		for lineas in archivo.readlines():
			#lineV,lineF = lineas.split(' ',1)

			#Lineas con valores de V
			#Para realizar este algoritmo se utilizo el ejemplo de abajo
			if(lineas[0] == 'v' and lineas[0] != 'n'):
				lineV = lineas.split(' ')
				#contador para los valores
				n = 1
				#vertice = [x,y]
				self.vertices.append(((float(lineV[n])),((float(lineV[n+1])))))
			#Lineas con valores de F
			if(lineas[0] == 'f'):
				lineF = lineas.split(' ')
				face = lineF.pop(0)
				face = []
				#Ciclo para quitar lo parametro extras
				for i in lineF:
					i = i.split("/")
					#El valor sera guardado en una lista
					face.append(int(i[0]))
				self.faces.append(face)
				#self.faces.append([list(map(int, face.split('/'))) for face in lineas[0].split(' ')])
		#Cerramos el archivo
		archivo.close()
"""
#-------- INTENTO CON SOLO UNA LINEA ----------#
#vertice = []
#lineas = 'v 0.376516 1.770015 -2.274176'
#valor = lineas.split(" ")
#valor_x = valor.pop(1)
#valor_Y = valor.pop(2)
#vertice.append((float(valor_x),float(valor_Y)))
#print(vertice)

#-------- INTENTO CON UN CICLO --------#
#faces = []
#contador = 1
#lineas = 'f 5//1 4//1 10//1 11//1'
#while(contador<2):
	#line = lineas.strip().split(' ')
	#if(line[0] == 'f'):
		#line.pop(0)
		#face = []
		#for i in line:
			#i = i.split("//")
			#face.append(int(i[0]))
		#faces.append(face)
	#print(faces)
	#contador +=1
