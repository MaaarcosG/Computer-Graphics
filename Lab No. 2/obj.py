# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

import struct

#Funcion de color
def color(r,g,b):
    return bytes([r, b , g])

# Funcion tomado de Clase, esta funciona encuentra los valores de la cara
# Y los transforma en base 10, para que la transfomaciones sean mas pequeñas
def try_int(s, base=10, valor=None):
    try:
        return int(s, base) -1
    except ValueError:
        return valor

"Clase que sirve para abrir un archivo obj"
class Obj(object):
    def __init__(self, filename, mtl=None):
        self.verificador = False
        #Condicion para abrir archivo obj
        with open(filename) as f:
            self.lines = f.read().splitlines()
        #Condicion para verificar que si hay un archivo mtl
        if mtl:
            self.verificador = True
            with open(mtl) as x:
                self.linea = x.read().splitlines()
        #Todos los datos se guardaran en un arraay
        self.vertices = []
        self.vt = []    #vertices
        self.faces = [] 
        self.tipoMateriales = []
        self.kD = []
        self.kdMap = []
        self.ordenarMateriales = []
        self.material = {}
        #inicializamos la funcion para leer
        self.read()

    #Funcion para leer archivo
    def read(self):
        self.mater = ''

        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    #Guardamos los datos en la lista
                    self.vertices.append(list((map(float, value.split(' ')))))
                elif prefix == 'vt':
                    #Guardamos los datos en la lista
                    self.vt.append(list((map(float, value.split(' ')))))
                elif prefix == 'f':
                        if self.verificador == False:
                            self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])
                        else:
                            lista = [list(map(int, face.split('/'))) for face in value.split(' ')]
                            lista.append(self.mater)
                            self.faces.append(lista)

                elif prefix == 'usemtl':
                    self.mater = value

        if self.verificador:
            for line2 in self.linea:
                if line2:
                    prefix2, valor = line2.split(' ', 1)
                    if prefix2 == 'newmtl':
                        self.tipoMateriales.append(valor)
                    if prefix2 == 'Kd':
                        self.kD.append(list(map(float, valor.split(' '))))
                        '''
                    if prefix2 == 'map_Kd':
                        self.kdMap.append(list(map(float, valor.split(' '))))
                    print(self.kdMap)
                    '''
            for indice in range(len(self.tipoMateriales) - 1):
                self.material[self.tipoMateriales[indice]] = self.kD[indice]
