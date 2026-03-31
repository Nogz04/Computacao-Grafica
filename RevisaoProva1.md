# Guia de Estudo: Computação Gráfica (Revisão Prova 01)
**Instituição:** Universidade Franciscana - UFN  
**Estudante:** Matheus Nogueira Albuquerque  
**Professor:** André F. dos Santos

---

## 1) Objetivo das Transformações Geométricas
**Questão:** Qual é o objetivo das transformações geométricas em Computação Gráfica? Como elas são aplicadas e a que movimentos estão relacionadas?

**Resposta e Explicação:**
O objetivo principal é manipular objetos em um espaço 2D ou 3D, alterando sua **posição**, **orientação** ou **tamanho**. Elas são a base para criar animações (movimento) e modelar cenas complexas.

Os movimentos fundamentais são:
* **Translação:** Move o objeto somando um deslocamento $(\Delta x, \Delta y)$ às coordenadas originais.
* **Rotação:** Gira o objeto em torno de um ponto fixo usando funções trigonométricas (seno e cosseno).
* **Escala:** Altera o tamanho multiplicando as coordenadas por fatores de escala.



---

## 2) O Processo de Clipping (Recorte)
**Questão:** Qual é a importância do processo de clipping e onde ele pode ser aplicado?

**Resposta e Explicação:**
O **Clipping** serve para descartar tudo o que está fora da área de visão (a "janela" ou *viewport*). 
* **Importância:** Economiza processamento. Se o computador não precisa desenhar o que você não está vendo, o sistema fica muito mais rápido.
* **Aplicações:** Jogos 3D (objetos atrás da câmera são ignorados) e softwares de design (como Photoshop, onde o que está fora da tela não é renderizado).

---

## 3) Translação (Múltipla Escolha)
**Questão:** A translação em Computação Gráfica:
**Resposta:** **b) Define a posição de um objeto no universo.**

**Explicação:** Diferente da escala ou rotação, a translação apenas "teletransporta" o objeto de um lugar para outro sem mudar sua aparência ou tamanho.

---

## 4) Equações de Escala (Múltipla Escolha)
**Questão:** Como a escala é definida e aplicada considerando as equações $x_u = x_0 \cdot s_x$ e $y_u = y_0 \cdot s_y$?
**Resposta:** **c) A escala é a modificação do tamanho de um objeto, utilizando as equações nos pontos do objeto.**

**Explicação:** O fator $s$ funciona como um multiplicador. Se $s = 2$, o objeto dobra de tamanho. Se $s = 0.5$, ele cai pela metade.

---

## 5) Rasterização (Múltipla Escolha)
**Questão:** O que representa o processo de rasterização?
**Resposta:** **a) Um método para converter imagens vetoriais em formatos de mapa de bits.**

**Explicação:** Vetores são cálculos matemáticos perfeitos. Rasterizar é "traduzir" esses cálculos para os pixels (pontos) da sua tela física.

---

## 6) Algoritmo Natural de Linhas
**Questão:** No cenário onde a inclinação $m \le 1$ (ângulo $\le 45^\circ$):
**Resposta:** **a) "x" cresce mais rápido que "y" na reta, portanto, precisamos calcular para cada "x" o valor de "y" correspondente.**

**Explicação:** Se a linha é mais horizontal do que vertical, para cada pixel que avançamos no eixo X, calculamos onde o Y deve ficar para manter a linha reta.

<img width="510" height="328" alt="image" src="https://github.com/user-attachments/assets/efbdc784-5e71-4531-8058-e8fd296b1eb8" />



---

## 7) Importância dos Círculos
**Questão:** Por que os círculos são fundamentais?
**Resposta:** **c) Possibilitam a geração de curvas suaves e superfícies complexas.**

**Explicação:** Sem círculos e curvas, tudo no computador seria feito de quadrados e triângulos pontiagudos. Eles permitem formas orgânicas e arredondadas.

---

## 8) O Papel das Matrizes
**Questão:** Por que o uso de matrizes é fundamental?
**Resposta:** **b) Facilitam a manipulação e transformação de objetos no espaço 2D e 3D.**

**Explicação:** As matrizes permitem que o computador faça cálculos de translação, rotação e escala de forma simultânea e organizada, tratando o objeto como um único bloco de dados.

---

## 9) Matriz de Transformação Composta
**Questão:** Explique a importância da matriz de transformação e como ela facilita múltiplas transformações.

**Resposta e Explicação:**
A grande vantagem é a **eficiência**. Em vez de calcular a posição do objeto após a translação, depois calcular novamente para a rotação e depois para a escala, nós multiplicamos as matrizes de cada transformação primeiro. O resultado é uma única "Matriz Mestra" que, aplicada ao objeto, realiza todas as mudanças de uma só vez, economizando tempo de CPU/GPU.

---

## 10) Etapas de Visualização
**Questão:** Qual etapa converte coordenadas 3D em uma projeção 2D?
**Resposta:** **c) Projeção.**

**Explicação:** É o processo de "achatar" o mundo 3D para que ele caiba na superfície plana do seu monitor.

---

## 11) Projeção Paralela vs. Perspectiva
**Questão:** Descreva a diferença entre as duas e cite exemplos.

**Resposta e Explicação:**
* **Projeção Paralela:** Não distorce o tamanho com a distância. Essencial para **Engenharia (CAD)** e desenhos técnicos onde as medidas precisam ser exatas.
* **Projeção Perspectiva:** Objetos longe parecem menores. Usada em **Cinema e Jogos** para simular a visão humana e dar profundidade à cena.

[Image comparing parallel projection versus perspective projection]

---

## 12) Exercício de Translação 3D
**Questão:** Dado o ponto $P=(2, -3, 5, 1)$, aplique translação com $T_x=3, T_y=4, T_z=-2$.

**a) Matriz de Translação ($M_t$):**
A matriz de translação utiliza a última coluna para os fatores de deslocamento:

$$
M_t = \begin{pmatrix}
1 & 0 & 0 & 3 \\
0 & 1 & 0 & 4 \\
0 & 0 & 1 & -2 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**b) Cálculo do novo ponto $P'$:**
Multiplicamos a matriz pelo ponto (em formato de coluna):

$$
\begin{pmatrix} 1 & 0 & 0 & 3 \\ 0 & 1 & 0 & 4 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ -3 \\ 5 \\ 1 \end{pmatrix} = \begin{pmatrix} (1 \cdot 2) + 3 \\ (1 \cdot -3) + 4 \\ (1 \cdot 5) - 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \\ 3 \\ 1 \end{pmatrix}
$$

**Resultado:** $P' = (5, 1, 3, 1)$

---

## 13) Exercício de Escala 3D
**Questão:** Aplicar escala uniforme de $0.5$ ao ponto $P=(10, 20, 30, 1)$.

**a) Matriz de Escala ($M_s$):**
Os fatores de escala ficam na diagonal principal:

$$
M_s = \begin{pmatrix}
0.5 & 0 & 0 & 0 \\
0 & 0.5 & 0 & 0 \\
0 & 0 & 0.5 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**b) Cálculo do novo ponto $P'$:**
Basta multiplicar cada coordenada pelo fator $0.5$:

* $x' = 10 \cdot 0.5 = 5$
* $y' = 20 \cdot 0.5 = 10$
* $z' = 30 \cdot 0.5 = 15$

**Resultado:** $P' = (5, 10, 15, 1)$

---

## 14) Rotação e Identificação de Eixo
**Questão:** Identifique em relação a qual eixo a matriz abaixo está operando:

$$
Mat = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**Resposta:** **Eixo X.**

**Justificativa Didática:** Observe a primeira linha e a primeira coluna. Elas contêm o valor **1** na diagonal e **0** ao redor. Isso significa que, ao multiplicar qualquer ponto por essa matriz, a coordenada **X permanecerá idêntica**. Se o X não muda, o objeto está girando "em volta" do eixo X. Os valores de seno e cosseno estão nas posições que afetam Y e Z, confirmando a rotação nesse plano.
