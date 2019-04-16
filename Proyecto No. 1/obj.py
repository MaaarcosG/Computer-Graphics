# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

import struct
import mmap
import numpy
#Funcion de color
def color(r,g,b):
    return bytes([r, b , g])

"Clase que sirve para abrir un archivo obj"
class Obj(object):
    def __init__(self, filename):
        #Condicion para abrir archivo obj
        with open(filename) as f:
            self.lines = f.read().splitlines()
        #Todos los datos se guardaran en un arraay
        self.vertices = []
        self.vt = []    #tvertices
        self.faces = []
        #inicializamos la funcion para leer
        self.read()

    #Funcion para leer archivo
    def read(self):
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
                    #Guardamos los datos en la lista
                    self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])

'Clase para leer un archivo bmp'
class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        img = open(self.path, "rb")
        m = mmap.mmap(img.fileno(), 0, access=mmap.ACCESS_READ)
        ba = bytearray(m)
        header_size = struct.unpack("=l", ba[10:14])[0]
        self.width = struct.unpack("=l", ba[18:22])[0]
        self.height = struct.unpack("=l", ba[18:22])[0]
        all_bytes = ba[header_size::]
        self.pixels = numpy.frombuffer(all_bytes, dtype='uint8')
        img.close()

    def get_color(self, tx, ty, intensity):
        x = int(tx * self.width)
        y = int(ty * self.height)
        index = (y * self.width + x) * 3
        processed = self.pixels[index:index+3] * intensity
        return bytes(processed.astype(numpy.uint8))
