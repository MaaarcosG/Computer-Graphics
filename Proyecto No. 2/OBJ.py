import numpy as np

# Clase obj para cargar los componentes de un archivo obj
class Obj:
    def __init__(self):
        self.vertices = []
        self.texturas = []
        self.nc = []
        self.vertexIndex = []
        self.textureIndex = []
        self.normalIndex = []
        self.model = []

    def load(self, file):
        # Ciclo para recorrer cada uno de los datos
        for line in open(file, 'r'):
            if line.startswith('#'): continue

            # Variable para separar cada dato
            values = line.split()
            if not values: continue

            # Vertices que los guardamos en una lista
            if values[0] == 'v':
                self.vertices.append(values[1:4])
            # Las coordenadas de las texturas que se guardan en una lista
            if values[0] == 'vt':
                self.texturas.append(values[1:3])

            # Los vectorens normales que las guardamos en una lista
            if values[0] == 'vn':
                self.nc.append(values[1:4])

            # F se relaciona con las caras de los objetos
            if values[0] == 'f':
                # Variables para unir cada uno de los y hacerlas caras
                faces = []
                vt = []
                nt = []
                for value in values[1:4]:
                    separaEspacios = value.split('/')
                    faces.append(int(separaEspacios[0])-1)
                    vt.append(int(separaEspacios[1])-1)
                    nt.append(int(separaEspacios[2])-1)

                # Guardamos cada cara en una lista
                self.vertexIndex.append(faces)
                self.textureIndex.append(vt)
                self.normalIndex.append(nt)

        self.vertexIndex = [y for x in self.vertexIndex for y in x]
        self.textureIndex = [y for x in self.textureIndex for y in x]
        self.normalIndex = [y for x in self.normalIndex for y in x]

        # Recorremos los datos del vertex Index
        for i in self.vertexIndex:
            self.model.extend(self.vertices[i])

        # Recorremos los datos de las texturas
        for i in self.textureIndex:
            self.model.extend(self.texturas[i])

        # Recorremos los datos de normal index
        for i in self.normalIndex:
            self.model.extend(self.nc[i])

        # Guardamos los datos y los 
        self.model = np.array(self.model, dtype='float32')
