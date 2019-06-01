'''
 Universidad del Valle de Guatemala
 Graficas Por Computadoras
 Proyecto No. 2
    Marcos Gutierrez
    17909
'''

#---------- Importamos librerias de Python ----------#
import glfw
import numpy
from pyrr import matrix44, Vector3, Matrix44
#---------- Importamos librerias de OpenGL ----------#
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
#---------- Funciones extras para movimiento --------#
from OBJ import *
from MOVIMIENTO import Camera
import TEXTURE as tex

#-Variables Globales para los vectores de movimiento-#
# Estos vectores se implementaran en la matriz de lookAt
position = Vector3([0, 0, 30])
frontal = Vector3([0, 0, -1])
arriba = Vector3([0, 1, 0])
derecha = Vector3([1, 0, 0])

# Variables globles
camara = Camera()
rotation = False
# Variable para tener las llaves de la ventana
keys = [False] * 1024
# Valores obtenidos del tamano de la ventana
valorX = (1080/2)
valorY = (720/2)
# Condicion por si encuentra un mouse
mouse = True

# Funcion que ayuda a habilitar las teclas de la ventana
def habilitacion(ventana, key, scancode, action, mode):
    if (key >= 0) and (key < 1024):
        if action == glfw.PRESS:
            keys[key] = True
        elif action == glfw.RELEASE:
            keys[key] = False

# https://www.glfw.org/docs/latest/group__keys.html  (Link que brinda cada una de las teclas)
def do_movement():
    # Variables globales para el movimiento de la camara
    global position, frontal, arriba, derecha, rotation

    # Si ejecuta la flecha W
    if keys[glfw.KEY_W] or keys[glfw.KEY_UP]:
        camara.teclado("ADELANTE")
    # Si ejecuta la flecha S
    if keys[glfw.KEY_S] or keys[glfw.KEY_DOWN]:
        camara.teclado("ATRAS")
    # Si ejecuta la flecha A
    if keys[glfw.KEY_A] or keys[glfw.KEY_LEFT]:
        camara.teclado("IZQUIERDA")
    # Si ejecuta la flecha D
    if keys[glfw.KEY_D] or keys[glfw.KEY_RIGHT]:
        camara.teclado("DERECHA")
    # Si ejecuta la tecla F rellena el modelo
    if keys[glfw.KEY_F]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # Si ejecuta la tecla L vuelve todo en linea
    if keys[glfw.KEY_L]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if keys[glfw.KEY_R]:
        rotation = True


def uso_mouse(ventana, xpos, ypos):
    global mouse, valorX, valorY
    # Si hay un mouse da los valores en x e y
    if mouse:
        valorX = xpos
        valorY = ypos
        mouse = False
    # Valores de x
    delta_x = xpos - valorX
    # Valores de y
    delta_y = valorY - ypos
    # Variables para optener cada uno de los valores
    valorX = xpos
    valorY = ypos
    camara.mouseMovimiento(delta_x, delta_y)


def main():
    # Inicializamos la libreria de glfw
    if not glfw.init():
        return

    ventana = glfw.create_window(1080, 720, "Main window", None, None)

    # Funciones principales de glfw para en la ventana
    glfw.make_context_current(ventana)
    # Funcion para habilitar las teclas de la ventana
    glfw.set_key_callback(ventana, habilitacion)
    # Da la posicion del mouse tanto en x e y
    glfw.set_cursor_pos_callback(ventana, uso_mouse)
    glfw.set_input_mode(ventana, glfw.CURSOR, glfw.CURSOR_DISABLED)

    # Leemos el objeto, se utilizo como alternativa a pyassimp
    objeto = Obj()
    objeto.load("./objetos/wembley.obj")
    # Leemos la textura, se utilizo como alternativa
    objeto_texture = tex.texture("./objetos/wembley.jpg")
    objeto_texture_offset = len(objeto.vertexIndex) * 12

    # Creamos cada uno de los shaders
    generic_vertex = '''
        #version 440
        in layout(location = 0) vec3 position;
        in layout(location = 1) vec2 textureCoords;

        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        uniform vec4 color;
        uniform vec4 light;

        out vec4 vertexColor;
        out vec2 nTexture;

        void main()
        {
            gl_Position = projection * view * model * vec4(position, 1.0f);
            nTexture = vec2(textureCoords.x, 1 - textureCoords.y);
        }
    '''

    generic_fragment = '''
        #version 440
        in vec2 nTexture;

        out vec4 outColor;
        uniform sampler2D samplerTexture;

        void main()
        {
            outColor = texture(samplerTexture, nTexture);
        }
    '''

    shader = shaders.compileProgram(
        shaders.compileShader(generic_vertex, GL_VERTEX_SHADER),
        shaders.compileShader(generic_fragment, GL_FRAGMENT_SHADER),
    )

    # Lectura de Textura
    objetoVertex = glGenVertexArrays(1)
    glBindVertexArray(objetoVertex)
    objetoBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, objetoBuffer)
    glBufferData(GL_ARRAY_BUFFER, objeto.model.itemsize * len(objeto.model), objeto.model, GL_STATIC_DRAW)
    # Posicion del objeto
    glVertexAttribPointer(
        0,
        3,
        GL_FLOAT,
        GL_FALSE,
        objeto.model.itemsize * 3,
        ctypes.c_void_p(0)
    )
    glEnableVertexAttribArray(0)
    # Textura del objeto
    glVertexAttribPointer(
        1,
        2,
        GL_FLOAT,
        GL_FALSE,
        objeto.model.itemsize * 2,
        ctypes.c_void_p(objeto_texture_offset)
    )
    glEnableVertexAttribArray(1)
    glBindVertexArray(0)

    glClearColor(0.18, 0.18, 0.18, 1.0)
    glEnable(GL_DEPTH_TEST)

    # Utilizamos la libreria de pyrr para la creacion de la matrix
    projectionMatrix = matrix44.create_perspective_projection_matrix(
        45.0,
        (1080/720),
        0.1,
        100.0
    )
    # Model matrix
    MM = Vector3([0.0, 0.0, -10.0])
    modelMatrix = matrix44.create_from_translation(MM)

    # Utilizamos shader para la compilacion
    glUseProgram(shader)

    # Matrix de projection
    glUniformMatrix4fv(
        glGetUniformLocation(shader, "projection"),
        1,
        GL_FALSE,
        projectionMatrix
    )

    # Ciclo para evitar que se trabe la libreria glfw
    while not glfw.window_should_close(ventana):
        # Obtenemos cada uno de los eventos
        glfw.poll_events()
        do_movement()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = camara.viewMatriz()

        # Matrix de view
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "view"),
            1,
            GL_FALSE,
            view
        )

        if rotation == False:
            do_movement()
            rotationY = Matrix44.from_y_rotation(glfw.get_time() * 0.5)
            glUniformMatrix4fv(
                glGetUniformLocation(shader, "model"),
                1,
                GL_FALSE,
                rotation*modelMatrix
            )

        # Utilizamos las libreris de OpenGL para obtener las texturas
        glBindVertexArray(objetoVertex)
        glBindTexture(GL_TEXTURE_2D, objeto_texture)

        # Creamos la matrix del modelo
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "model"),
            1,
            GL_FALSE,
            modelMatrix
        )
        # Dibujamos cada uno de los triangulos
        glDrawArrays(GL_TRIANGLES, 0, len(objeto.vertexIndex))
        glBindVertexArray(0)

        # Mandamos cada uno de los buffers
        glfw.swap_buffers(ventana)

    glfw.terminate()


print(
    '''
    Bienvenido, cualquier consulta o alguna duda porfavor leea el README.txt que se
    encuentra en la misma carpeta que se encuentra este programa.
    '''
)
main()
