import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# ===  EX7) Alterei a posição inicial do triângulo para o centro da tela mudando o valor de X de -1.5 para 0, agora o triangulo inicia no centro da tela === 
x = 0 # Aqui o X era -1.5 (mudei para 0)
y = 0 # Aqui o Y já era 0
r = 0

# ===  EX8) Mudei o valor de ex, ey e ez para 2, agora o triângulo inicia maior === 
ex = 2 # Aqui o ex era 1 (mudei para 2)
ey = 2 # Aqui o ey era 1 (mudei para 2)
ez = 2 # Aqui o ez era 1 (mudei para 2)

# ===  EX10) Variável de Zoom ===
zoom = -6 

def init():
    
    # ===  EX1) Alterar cor do FUNDO para branco ===
    glClearColor(1.0, 1.0, 1.0, 1.0);   # Cor de FUNDO branca 


    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()
    # === EX10) Uso da variável zoom na translação ===
    glTranslatef(x, y, zoom)

    # ===  EX2) Mudei a rotação do eixo Y para o X ===
    # O triângulo vai girar como se estivesse dando cambalhotas para trás (descomentar linha para ativar - e comentar a la de baixo)
    # glRotatef(r, 1, 0, 0)  
    
    # ===  EX3) Mudei a rotação do eixo Y para o eixo X e Y ===
    # Agora o triangulo irá girar como se fosse uma bailarina, em uma posição de 45 graus girando em diagonal 
    glRotatef(r, 1, 1, 0)  

    glScalef(ex, ey, ez)
    glBegin(GL_TRIANGLES)

    # ===  EX4) Alterar cor do triângulo para preto ===
    glColor3f(0, 0, 0)  # Cor preta

    # ===  EX5) Alterei os vertices X e Y para um número maior ===
    glVertex3f(0, 2, 0)
    glVertex3f(-2, -2, 0)
    glVertex3f(2, -2, 0)


    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    global x, y, r, ex, ey, ez, zoom

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                # ===  EX9) Inverti os controles A e D ===
                if event.key == K_a:
                    x += 0.2 # Agora o A move para a DIREITA
                if event.key == K_d:
                    x -= 0.2 # # Agora o D move para a ESQUERDA
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y += -0.2
                
                # === EX10) Controles de Zoom Z e X ===
                if event.key == K_z:
                    zoom += 0.2 # Aproxima (traz para frente)
                if event.key == K_x:
                    zoom -= 0.2 # Afasta (empurra para trás)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5:
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw()

        pygame.display.flip()

        pygame.time.wait(10)


        # ===  EX6) Mudei a rotação para girar em sentido anti-horário 
        # (mudamos apenas o sinal de r += para r -= e adicionamos um valor maior(10) para aumentar a velocidade) ===
        r -= 10 

    pygame.quit()

if __name__ == "__main__":
    main()
