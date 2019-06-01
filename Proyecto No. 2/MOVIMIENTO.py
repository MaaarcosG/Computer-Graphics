'''
 Universidad del Valle de Guatemala
 Graficas Por Computadoras
 Proyecto No. 2
    Marcos Gutierrez
    17909
'''

#------- Liberias necesarias para la Python -------#
from pyrr import Vector3, Matrix44, vector, vector3
from math import sin, cos, radians


class Camera:
    def __init__(self):
        #--------------- Vectores para cada una de las posiciones ----------------------#
        self.posicion = Vector3([0.0, 0.0, 30.0])
        self.frontal = Vector3([0.0, 0.0, -1.0])
        self.arriba = Vector3([0.0, 1.0, 0.0])
        self.derecha = Vector3([1.0, 0.0, 0.0])

        self.sensibilidad = 0.25
        self.dataX = -90.0
        self.dataY = 0.0

    def viewMatriz(self):
        return self.lookAtMe(self.posicion, (self.posicion + self.frontal), self.arriba)

    def teclado(self, direction):
        # Condicion para adelante
        if direction == "ADELANTE":
            self.posicion -= self.frontal * 0.1
            # debug ---->print(self.posicion)
            # Condicion para evitar de que el modelo desaparesca
            if self.posicion.z < 2:
                self.posicion = Vector3([0.0, 0.0, 30.0])

        # Condicion para atras
        if direction == "ATRAS":
            self.posicion += self.frontal * 0.1
            # debug ---->print(self.posicion)
            # Ciclo para evitar que desaparesca el modelo
            if self.posicion.z > 85:
                self.posicion = Vector3([0.0, 0.0, 30.0])

        # Condicion para la izquierda
        if direction == "IZQUIERDA":
            # Condicion para evitar de que el modelo desaparesca
            self.posicion += self.derecha * 0.1
            # debug ----> print(self.posicion)
            if self.posicion.x > 28:
                self.posicion = Vector3([0.0, 0.0, 30.0])

        # Condcion para la derecha
        if direction == "DERECHA":
            self.posicion -= self.derecha * 0.1
            # debug ---> print(self.posicion)
            # Condicion para evitar de que el modelo desaparesca
            if self.posicion.x < -25:
                self.posicion = Vector3([0.0, 0.0, 30.0])

    def mouseMovimiento(self, xoffset, yoffset, detector=True):
        # Valores del mouse
        xoffset = xoffset * self.sensibilidad
        yoffset = yoffset * self.sensibilidad

        self.dataX = self.dataX + xoffset
        self.dataY = self.dataY + yoffset

        # Si detecta un mouse que tome los siguientes datos
        if detector:
            # Si el dato es mayor o menor al dato en y que tome los datos
            if(self.dataY > 45.0):
                self.dataY = 45.0
            if (self.dataY < -45.0):
                self.dataY = -45.0

        # Vector para la camara frontal
        front = Vector3([0.0, 0.0, 0.0])
        # Encontramos cada uno de los datos de la camara front tanto en x, y e z
        front.x = cos(radians(self.dataX)) * cos(radians(self.dataY))
        front.y = sin(radians(self.dataY))
        front.z = sin(radians(self.dataX)) * cos(radians(self.dataY))

        # Normalizamos el vector, para obtener datos cercanos
        # debug ---> print(self.frontal)
        self.frontal = vector.normalise(front)
        # debug ---> print(self.derecha)
        # debug ---> print(self.arriba)
        self.derecha = vector.normalise(vector3.cross(self.frontal, Vector3([0.0, 1.0, 0.0])))
        self.arriba = vector.normalise(vector3.cross(self.derecha, self.frontal))

    def lookAtMe(self, position, target, world_up):
        # Calculamos la direccion de la camara en z
        zaxis = vector.normalise(position - target)
        # Calculamos la direccion de la camara en x
        xaxis = vector.normalise(vector3.cross(vector.normalise(world_up), zaxis))
        # Calculamos la direccion de la camara en y
        yaxis = vector3.cross(zaxis, xaxis)

        # Creamos la matriz de transaltion y de rotation
        translation = Matrix44.identity()
        rotation = Matrix44.identity()
        '''
        matrix identidad = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
        '''
        # Dentro de la matriz ingresamos cada uno de los valores
        translation[3][0] = -position.x
        translation[3][1] = -position.y
        translation[3][2] = -position.z

        # Añadimos a la matriz los valores
        rotation[0][0] = xaxis[0]
        rotation[1][0] = xaxis[1]
        rotation[2][0] = xaxis[2]
        rotation[0][1] = yaxis[0]
        rotation[1][1] = yaxis[1]
        rotation[2][1] = yaxis[2]
        rotation[0][2] = zaxis[0]
        rotation[1][2] = zaxis[1]
        rotation[2][2] = zaxis[2]

        return translation * rotation
