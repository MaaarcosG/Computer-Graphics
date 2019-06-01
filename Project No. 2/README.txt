!Hola Bienvenido!
El programa principial es el llamado openGL.py antes de poder ejecutarlo se necesita instalar algunas librerias externas
  --> pyrr (pip install pyrr)		Libreria para la crear la pantalla
  --> glfw (pip install pyGLFW)		Libreria matematica para matrices y 					vectores

TECLAS PARA UTILIZACIÓN
  --> Tecla W o TECLA UP 	hace que el objeto se vaya para adelante
  --> Tecla S o TECLA DOWN 	hace que el objeto se vea de lejos
  --> Tecla D o TECLA RIGHT	hace que el objeto se mueva para la derecha
  --> Tecla A o TECLA LEFT 	hace que el objeto se mueva para la izquierda

Cada vez de que objeto se mueva tanto con las teclas de W, S, D, A cuando los objetos estan apunto de desaparecer vuelve a
al tamaño original. 

PARA MAYOR PRUEBAS:
	line 108   objeto.load("./objetos/vecchio.obj")
	line 110   tex.texture("./objetos/gris.jpg")

OBSERVACION: El proyecto es posible el movimiento con el mouse, pero con un pequeño bug, es que si se mueve demasiado la 
pantalla junto con el objeto, el objeto tiende a desaparecer.