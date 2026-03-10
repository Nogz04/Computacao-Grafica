# Relatório de Exercícios - Computação Gráfica (Aula 03)

Este documento resume as alterações realizadas no arquivo `TesteOpenGl.py` para os exercícios 1 a 10.

---

### EX1) Alterar cor do fundo para branco
*   **Antes:** `glClearColor(0.0, 0.0, 0.0, 1.0)` (Preto)
*   **Depois:** `glClearColor(1.0, 1.0, 1.0, 1.0)`
*   **O que aconteceu:** O fundo da janela passou de preto para branco absoluto.

### EX2) Mudar rotação do eixo Y para o eixo X
*   **Antes:** `glRotatef(r, 0, 1, 0)`
*   **Depois:** `glRotatef(r, 1, 0, 0)`
*   **O que aconteceu:** O triângulo parou de girar como um "pião" (lado a lado) e passou a dar "cambalhotas" (para frente/trás).

### EX3) Mudar rotação para os eixos X e Y simultaneamente
*   **Antes:** `glRotatef(r, 1, 0, 0)`
*   **Depois:** `glRotatef(r, 1, 1, 0)`
*   **O que aconteceu:** O triângulo passou a girar em uma diagonal de 45 graus, combinando os dois movimentos anteriores.

### EX4) Alterar cor do triângulo para preto
*   **Antes:** `glColor3f(1, 1, 0)` (Amarelo)
*   **Depois:** `glColor3f(0, 0, 0)`
*   **O que aconteceu:** O triângulo ficou totalmente preto, criando um contraste com o fundo branco.

### EX5) Aumentar o tamanho dos vértices
*   **Antes:** `(0, 1, 0)`, `(-1, -1, 0)`, `(1, -1, 0)`
*   **Depois:** `(0, 2, 0)`, `(-2, -2, 0)`, `(2, -2, 0)`
*   **O que aconteceu:** O triângulo dobrou de tamanho na tela, pois os pontos que o definem foram afastados do centro.

### EX6) Rotação mais rápida e no sentido horário
*   **Antes:** `r += 3` (Sentido anti-horário, lento)
*   **Depois:** `r -= 10`
*   **O que aconteceu:** O sinal `-` inverteu o sentido da rotação para horário e o valor `10` triplicou a velocidade do movimento.

### EX7) Alterar posição inicial para o centro
*   **Antes:** `x = -1.5`
*   **Depois:** `x = 0`
*   **O que aconteceu:** Ao iniciar o programa, o triângulo agora aparece centralizado na tela em vez de deslocado para a esquerda.

### EX8) Alterar escala inicial (Zoom inicial)
*   **Antes:** `ex = 1, ey = 1, ez = 1`
*   **Depois:** `ex = 2, ey = 2, ez = 2`
*   **O que aconteceu:** O triângulo inicia o programa com o dobro do tamanho original (escala 2x).

### EX9) Inverter controles A e D
*   **Antes:** `A` (x -= 0.2), `D` (x += 0.2)
*   **Depois:** `A` (x += 0.2), `D` (x -= 0.2)
*   **O que aconteceu:** Os controles foram invertidos: pressionar a tecla da esquerda (A) move o objeto para a direita e vice-versa.

### EX10) Controle de Zoom com 'Z' e 'X'
*   **Implementação:** Criada variável `zoon = -6`, usada em `glTranslatef(x, y, zoon)`.
*   **Comandos:** Tecla `Z` faz `zoon += 0.2` e Tecla `X` faz `zoon -= 0.2`.
*   **O que aconteceu:** Agora é possível aproximar (Z) e afastar (X) o triângulo da "câmera" alterando sua profundidade no eixo Z.

---
## Código Final (todos os exercicios feitos na prática):

> NOME: Matheus Nogueira Albuquerque
> 
> DATA: 10/03/2026

```python
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

```
