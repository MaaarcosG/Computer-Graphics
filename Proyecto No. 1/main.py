from bmp import *


r = Bitmap(800, 800)
t = Texture('./models/goku.bmp')

r.load('./models/goku.obj', (1,1,1), (300,300,300), texture=t)
r.archivo('prueba.bmp')
