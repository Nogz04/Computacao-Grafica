# Relatório de Pesquisa: Algoritmo de Rasterização de Bresenham

## Explicação dos Algoritmos de Rasterização

A rasterização é o processo fundamental na computação gráfica de converter formas geométricas matemáticas (vetores) em uma grade de pixels para exibição em monitores.

### Algoritmo Natural
É o método mais básico, fundamentado na equação reduzida da reta ($y = mx + b$). Ele calcula o coeficiente angular ($m$) e o linear ($b$) para determinar a posição de cada ponto. Embora didático, é computacionalmente pesado por exigir multiplicações, divisões e arredondamentos para cada pixel processado.

### Algoritmo DDA (Digital Differential Analyzer)
O DDA melhora o desempenho ao utilizar a diferença incremental. Em vez de resolver a equação do zero a cada passo, ele entende que ao aumentar $x$ em $1$ unidade, o $y$ aumenta exatamente o valor do coeficiente $m$. Ele substitui a multiplicação por somas sucessivas, mas ainda depende de números decimais (ponto flutuante) e funções de arredondamento.

## 1. Nome do Algoritmo Encontrado
O algoritmo escolhido para esta pesquisa é o **Algoritmo de Reta de Bresenham** (também conhecido como Algoritmo do Ponto Médio).

## 2. Vantagens em Relação ao DDA
A principal vantagem do algoritmo de Bresenham é a sua **eficiência computacional extrema**. Diferente do DDA, que utiliza números decimais (ponto flutuante) e exige uma operação de arredondamento (`round`) a cada novo pixel, o Bresenham **não usa números decimais**. 

* **Velocidade:** Ele é consideravelmente mais rápido porque utiliza apenas aritmética de números inteiros (adição, subtração e multiplicação por 2, que o processador faz via deslocamento de bits). Isso elimina a necessidade de hardware especializado para cálculos reais.
* **Estética:** No que diz respeito à qualidade visual, a linha **não** fica mais bonita ou suave; ela apresenta o mesmo aspecto serrilhado ("escadinha") do DDA, pois ambos decidem apenas qual pixel deve ser totalmente pintado. Para suavidade, seriam necessários algoritmos de *Antialiasing*.



## 3. Critério de Decisão do Próximo Pixel
O algoritmo decide qual pixel pintar através de um **parâmetro de decisão (erro acumulado)**. Em vez de calcular o valor exato da coordenada $Y$, ele mantém uma variável que rastreia a distância entre a linha matemática ideal e o centro dos pixels disponíveis. 
A cada passo no eixo principal:
1. Ele verifica o sinal dessa variável de erro.
2. Se o erro indica que a linha está mais perto do pixel lateral, ele incrementa apenas um eixo.
3. Se o erro indica que a linha ultrapassou o ponto médio, ele incrementa ambos os eixos (movimento diagonal).
4. O erro é então atualizado para o próximo passo usando apenas somas e subtrações inteiras.

---

## 4. Código do algoritmo implementado (Java)

 Algoritmo de Bresenham, demonstrando como ele gerencia os diferentes casos de inclinação (octantes):

```java
void DrawLine(Vertex pixel1, Vertex pixel2, RGBA color1, RGBA color2) {
    // Calcula a variação de distância nos eixos X e Y
    int dx = pixel2.x - pixel1.x;
    int dy = pixel2.y - pixel1.y;
    int inclinacao = 0;    

    // Caso o ponto final venha antes do inicial no X, inverte os pontos para desenhar sempre da esquerda para a direita
    if(dx < 0) {
        DrawLine(pixel2, pixel1, color2, color1);
        return;
    }

    // Define se a reta sobe (1) ou desce (-1) conforme a variação de Y
    if(dy < 0) inclinacao = -1;
    else inclinacao = 1;

    int d; // Variável de decisão (erro acumulado)
    Vertex pixel = pixel1; // Inicia a partir do primeiro vértice

    PutPixel(pixel, color); // Pinta o primeiro pixel

    // CASO A: A reta é "deitada" (inclinação <= 45 graus ou |m| <= 1)
    if(dx >= Math.abs(dy)) {    
        if(dy < 0) { // Subcaso: a reta está descendo (y2 < y1)
            d = 2 * dy + dx; // Inicializa o erro para este sentido
            while(pixel.x < pixel2.x) { // Percorre o eixo X (eixo principal)
                if(d < 0) { // Se o erro for negativo, a linha está mais próxima da diagonal
                    d += 2 * (dy + dx); // Atualiza o erro acumulado
                    pixel.x++; // Avança no X
                    pixel.y--; // Desce no Y
                } else { // Se d >= 0, a linha está mais próxima da horizontal
                    d += 2 * dy; // Atualiza o erro
                    pixel.x++; // Avança apenas no X
                }
                PutPixel(pixel, color); // Pinta o pixel decidido
            }
        } 
        else { // Subcaso: a reta está subindo (y1 < y2)
            d = 2 * dy - dx; // Parâmetro de decisão inicial
            while(pixel.x < pixel2.x) { // Percorre o eixo X
                if(d < 0) { // O pixel mais próximo é o horizontal (Leste)
                    d += 2 * dy; // Soma a variação de Y ao erro
                    pixel.x++; // Incrementa apenas X
                } else { // O pixel mais próximo é o diagonal (Nordeste)
                    d += 2 * (dy - dx); // Ajusta o erro subtraindo a variação de X
                    pixel.x++; // Incrementa X
                    pixel.y++; // Incrementa Y
                }
                PutPixel(pixel, color); // Pinta o pixel decidido
            }
        }
    } 
    // CASO B: A reta é "em pé" (inclinação > 45 graus ou |m| > 1)
    else { 
        if(dy < 0) { // Subcaso: reta subindo verticalmente invertida
            d = dy + 2 * dx; // Inicializa erro com foco no eixo Y
            while(pixel.y > pixel2.y) { // Eixo principal de repetição passa a ser o Y
                if(d < 0) { // Se d < 0, move apenas verticalmente
                    d += 2 * dx; // Atualiza erro com base no deslocamento X
                    pixel.y--; // Decrementa Y
                } else { // Caso contrário, move na diagonal
                    d += 2 * (dy + dx); // Atualiza o erro total
                    pixel.x++; // Incrementa X
                    pixel.y--; // Decrementa Y
                }
                PutPixel(pixel, color); // Pinta o pixel decidido
            }
        } 
        else { // Subcaso: reta subindo verticalmente (y1 < y2)
            d = dy - 2 * dx; // Inicializa parâmetro de decisão
            while(pixel.y < pixel2.y) { // Percorre o eixo Y
                if(d < 0) { // Se d < 0, a reta inclinou o suficiente para mover em X
                    d += 2 * (dy - dx); // Atualiza erro
                    pixel.x++; // Incrementa X
                    pixel.y++; // Incrementa Y
                } else { // Se d >= 0, move apenas no eixo vertical
                    d += -2 * dx; // Ajusta o erro apenas pela variação de X
                    pixel.y++; // Incrementa apenas Y
                }
                PutPixel(pixel, color); // Pinta o pixel decidido
            }
        }
    }
    PutPixel(pixel2, color2); // Pinta o último pixel para garantir o fechamento da reta
}
