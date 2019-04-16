from bmp import *


r = Bitmap(800, 800)
t = Texture('./models/goku.bmp')
r.lookAt(V3(1, 0, 5), V3(0.5, 0, 0), V3(0, 1, 0))
r.load('./models/goku.obj', translate=(0,0,0), scale=(1,1,1), rotate=(0,0,0), texture=t)
r.archivo('prueba.bmp')
