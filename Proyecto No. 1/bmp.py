# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

from obj import *
from algebra import *
from math import cos, sin

"Clase que genera todos los datos"
class Bitmap(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.vertexColor = color(255,255,255)
        self.clear()
        #inicializamos las variables que serviran para el renderizado
        self.light = V3(0,1,1)
        self.activateTexture = None
        self.activateVertex = []

    #Funcion para limpiar
    def clear(self):
        self.framebuffer = [
            [color(0,0,0) for x in range(self.width)]
            for y in range(self.height)
        ]
        self.zbuffer = [[-float('inf') for x in range(self.width)] for y in range(self.height)]

    #Funcion para escribir
    def write(self, filename="out.bmp"):
        f = open(filename, 'bw')
        # File header (14 bytes)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))
        # Image header (40 bytes)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
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
    #Funcion para mostrar el archivo
    def archivo(self, filename='out.bmp'):
        self.write(filename)

    #Funcion para el color
    def set_color(self, color):
        self.vertexColor =color

    #Funcion para el puntos
    def point(self, x, y, color=None):
        self.framebuffer[y][x] = color or self.vertexColor

    #Funcion para dibujar triangulos
    def triangle(self, A, B, C, color=None, texture=None, texture_coords=(), intensity=1):
        '''
        A = next(self.activateVertex)
        B = next(self.activateVertex)
        C = next(self.activateVertex)
        #Condicion para encontrar los datos de un archivo Bitmap
        if self.activateTexture:
            tA = next(self.activateVertex)
            tB = next(self.activateVertex)
            tC = next(self.activateVertex)
        '''
        bbox_min, bbox_max = bbox(A, B, C)
        #Llenamos los poligonos con el siguiente Ciclo
        for x in range(bbox_min.x, bbox_max.x + 1):
            for y in range(bbox_min.y, bbox_max.y + 1):
                #Coordenads barycentricas
                w, v, u = baricentricas(A, B, C, V2(x,y))
                #Condicion para evitar numeros negativos
                if (w<0) or (v<0) or (u<0):
                    continue
                #Condicon para los datos de la textura
                if texture:
                    tA, tB, tC = texture_coords
                    tx = tA.x * w + tB.x * v + tC.x * u
                    ty = tA.y * w + tB.y * v + tC.y * u
                    #Mandamos los colores
                    color = texture.get_color(tx, ty, intensity)
                #Valores para la coordenada z
                z = A.z * w + B.z * v + C.z * u
                #Condicion para evitar numeros negativos
                if (x<0) or (y<0):
                    continue
                if x < len(self.zbuffer) and y < len(self.zbuffer[x]) and z > self.zbuffer[x][y]:
                    self.point(x, y, color)
                    self.zbuffer[x][y] = z

    '''
    MATRICES PARA LA VISUALIZACION DE LOS DATOS EN DIFERENTES POSICIONES
    '''
    def loadModelMatrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        #Mandamos los datos
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)
        #Matriz de translacion
        translatenMatrix = [
            [1, 0, 0, translate.x],
            [0, 1, 0, translate.y],
            [0, 0, 1, translate.z],
            [0, 0, 0,       1    ],
        ]
        #Matriz de escalar
        scaleMatrix = [
            [scale.x, 0, 0, 0],
            [0, scale.y, 0, 0],
            [0, 0, scale.z, 0],
            [0, 0,    0   , 1],
        ]
        #Matrices de rotacion tanto en x, y e z
        #X
        rotateMatriz_X = [
            [1,       0      ,        0      , 0],
            [0, cos(rotate.x), -sin(rotate.x), 0],
            [0, sin(rotate.x),  cos(rotate.x), 0],
            [0,       0      ,        0      , 1]
        ]
        #Y
        rotateMatriz_Y = [
             [ cos(rotate.y), 0,  sin(rotate.y), 0],
             [      0       , 1,        0      , 0],
             [-sin(rotate.y), 0,  cos(rotate.y), 0],
             [      0       , 0,        0      , 1]
        ]
        #Z
        rotateMatriz_Z = [
            [cos(rotate.z), -sin(rotate.z), 0, 0],
            [sin(rotate.z),  cos(rotate.z), 0, 0],
            [      0      ,        0      , 1, 0],
            [      0      ,        0      , 0, 1],
        ]
        #Matriz general de rotacion
        rotateMatriz = self.multiplicarMatrices(self.multiplicarMatrices(rotateMatriz_X, rotateMatriz_Y), rotateMatriz_Z)
        #Matriz general que contiene translate, scale, rotate
        self.Model = self.multiplicarMatrices(self.multiplicarMatrices(translatenMatrix, rotateMatriz), scaleMatrix)

    #Funcion para la viewMatrix
    def loadViewMatrix(self, x, y, z, center):
        M = [
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0],
            [ 0 ,  0 ,  0 , 1]
        ]
        O = [
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0,     1    ]
        ]
        #Multiplicamos las matrices para generar una sola
        self.View = self.multiplicarMatrices(M, O)

    #Funcion que contiene la matriz de projeccion
    def loadProjectionMatrix(self, coeff):
        self.Projection = [
            [1, 0,   0  , 0],
            [0, 1,   0  , 0],
            [0, 0,   1  , 0],
            [0, 0, coeff, 1]
        ]

    #Funcion que tiene la matriz de view port
    def loadViewportMatrix(self, x = 0, y = 0):
        self.Viewport = [
            [(self.width*0.5),         0        ,  0  ,  ( x+self.width*0.5) ],
            [       0        , (self.height*0.5),  0  ,  (y+self.height*0.5) ],
            [       0        ,         0        , 128 ,          128         ],
            [       0        ,         0        ,  0  ,          1           ]
        ]

    def trans(self, vertex, translate=(0,0,0), scale=(1,1,1)):
        return V3(
        round((vertex[0] + translate[0]) * scale[0]),
        round((vertex[1] + translate[1]) * scale[1]),
        round((vertex[2] + translate[2]) * scale[2])
        )

    #Funcion que tranforma las MATRICES
    def transform(self, vector):
        nuevoVector = [[vector.x], [vector.y], [vector.z], [1]]
        #Multiplicamos las diferentes matrices resultantes
        modelMultix = self.multiplicarMatrices(self.Viewport, self.Projection)
        viewMultix = self.multiplicarMatrices(modelMultix, self.View)
        vpMultix = self.multiplicarMatrices(viewMultix, self.Model)
        #Vector de transformacion
        vectores = self.multiplicarMatrices(vpMultix, nuevoVector)
        #transformacion
        transformVector = [
            round(vectores[0][0]/vectores[3][0]),
            round(vectores[1][0]/vectores[3][0]),
            round(vectores[2][0]/vectores[3][0])
        ]
        print(V3(*transformVector))
        #retornamos los Valores
        return V3(*transformVector)

    #Funcion para la vista
    def lookAt(self, eye, center, up):
        z = norm(sub(eye, center))
        x = norm(cross(up, z))
        y = norm(cross(z, x))
        self.loadViewMatrix(x, y, z, center)
        self.loadProjectionMatrix( -1 / length(sub(eye, center)))
        self.loadViewportMatrix()

    '''
    Funciones para cargar cada uno de los elementos
    '''
    def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), texture=None):
        objetos = Obj(filename)
        self.light = V3(0,0,1)

        for face in objetos.faces:
            vcount=len(face)

            if vcount == 3:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1

                a = self.trans(objetos.vertices[f1], translate, scale)
                b = self.trans(objetos.vertices[f2], translate, scale)
                c = self.trans(objetos.vertices[f3], translate, scale)

                vnormal = norm(cross(sub(b,a), sub(c,a)))
                intensity = dot(vnormal, self.light)

                if not texture:
                    grey =roun(255*intensity)
                    if grey<0:
                        continue
                    self.triangle(a,b,c, color=color(grey,grey,gey))
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    tA = V3(*objetos.vt[t1],0)
                    tB = V3(*objetos.vt[t2],0)
                    tC = V3(*objetos.vt[t3],0)

                    self.triangle(a,b,c, texture=texture, texture_coords=(tA,tB,tC), intensity=intensity)
            else:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1

                vertices = [
                    self.trans(objetos.vertices[f1], translate, scale),
                    self.trans(objetos.vertices[f2], translate, scale),
                    self.trans(objetos.vertices[f3], translate, scale),
                    self.trans(objetos.vertices[f4], translate, scale)
                ]
                normal = norm(cross(sub(vertices[0], vertices[1]), sub(vertices[1], vertices[2])))  # no necesitamos dos normales!!
                intensity = dot(normal, light)
                grey = round(255 * intensity)

                A, B, C, D = vertices

                if not texture:
                    grey = round(255 * intensity)
                    if grey < 0:
                        continue
                    self.triangle(A, B, C, color(grey, grey, grey))
                    self.triangle(A, C, D, color(grey, grey, grey))
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    t4 = face[3][1] - 1
                    tA = V3(*model.tvertices[t1])
                    tB = V3(*model.tvertices[t2])
                    tC = V3(*model.tvertices[t3])
                    tD = V3(*model.tvertices[t4])

                    self.triangle(A, B, C, texture=texture, texture_coords=(tA, tB, tC), intensity=intensity)
                    self.triangle(A, C, D, texture=texture, texture_coords=(tA, tC, tD), intensity=intensity)

    #------ FUNCIONES PARA TRABJAR CON MATRICES ------#
    # matriz uno = m1
    # matriz dos = m2

    #Comprobando teorema para crear una multiplicacion
    def teorema(self, filas, columna):
    	matriz = []
    	for i in range(filas):
    		#Añadimos una lista vacia
    		matriz.append([])
    		for j in range(columna):
    			matriz[-1].append(0.0)
    	#Retornamos la matriz creada
    	return matriz

    #Funcion para multiplicar las matrices
    def multiplicarMatrices(self, m1,m2):
    	#Condicion para multiplicar matrices es que el numero de columnas de una matriz debe ser el mismo que el numero de filas en la otra matriz
    	#Las matrices deben de tener la misma longitud (2x2 * 2x2).... (4x4 * 4x4)
    	#Basado en: https://www.geeksforgeeks.org/c-program-multiply-two-matrices/
    	"""
    		MATRIZ 1			MATRIZ 2
    	[ 0, 0 , 0 , 0 ]	[ 0, 0 , 0 , 0 ]
    	[ 0, 0 , 0 , 0 ]	[ 0, 0 , 0 , 0 ]
    	[ 0, 0 , 0 , 0 ]	[ 0, 0 , 0 , 0 ]
    	[ 0, 0 , 0 , 0 ]	[ 0, 0 , 0 , 0 ]
    	"""
    	matrizResultante = self.teorema(len(m1), len(m2[0]))
    	for i in range(len(m1)):
    		#Creamos la matriz
    		for j in range(len(m2[0])):
    			for k in range(len(m2)):
    				#damos valores a la matriz resultante
    				matrizResultante[i][j] += m1[i][k] * m2[k][j]
    	#retornmaos los resultados de la matriz
    	return matrizResultante