'''
 Universidad del Valle de Guatemala
 Graficas Por Computadoras
 Proyecto No. 2
    Marcos Gutierrez
    17909
'''

#---------- Importamos Librerias Extras de Python ----------#
from OpenGL.GL import *
from PIL import Image
import numpy


#Funcion que lee las texturas
def texture(path):
    # Le damos un valor a la funcion de OpenGL
    textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura)
    # Establecemos los parametros de texturas
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # Parametros de filtrados
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    # Cargamos la imagen utilizando PIL
    image = Image.open(path)
    imageData = numpy.array(list(image.getdata()), numpy.uint8)
    glTexImage2D(
        GL_TEXTURE_2D,          # Libreria de OpenGL
        0,
        GL_RGB,                 # Colores de RGB aplicados en OpenGL
        image.width,            # Ancho de la ventana
        image.height,           # Largo de la ventana
        0,
        GL_RGB,                 # OpenGL
        GL_UNSIGNED_BYTE,       # Obtenemos los bytes de la imagen
        imageData               # Variable de almacenaje de bytes
    )
    return textura
