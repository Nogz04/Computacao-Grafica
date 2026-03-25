# Relatório de Pesquisa: Algoritmos de Rasterização de Círculos
**Disciplina:** Computação Gráfica  
**Professor:** André F. dos Santos (UFN)  
**Estudante:** Matheus Nogueira Albuquerque  

---

## 1. Algoritmo de Círculo de Ponto Médio (Midpoint Circle)

### Como o algoritmo decide o pixel?
Diferente de funções contínuas, este algoritmo trabalha em uma grade discreta (pixels). Após pintar um pixel $(x, y)$, ele precisa decidir se o próximo será o **Leste** $(x+1, y)$ ou o **Sudeste** $(x+1, y-1)$.

Ele utiliza uma **função de decisão** baseada na equação da circunferência $f(x, y) = x^2 + y^2 - R^2$:
* O algoritmo avalia o valor desta função exatamente no **ponto médio** entre os dois pixels candidatos.
* **Se $f(ponto\_médio) < 0$**: O ponto médio está dentro do círculo ideal. Logo, o pixel de cima (Leste) está mais próximo da borda e é o escolhido.
* **Se $f(ponto\_médio) \ge 0$**: O ponto médio está fora ou sobre a borda. Isso indica que a curva está descendo, então o pixel de baixo (Sudeste) é o escolhido.



### Principal Vantagem: Simetria de 8 Oitantes
Um círculo possui simetria total. O algoritmo calcula apenas os pontos de um arco de 45° (1/8 do círculo). Os outros 7 oitantes são preenchidos por reflexão: se você tem $(x, y)$, você tem automaticamente $(-x, y)$, $(y, x)$, $(-y, -x)$, etc. Isso reduz a carga de processamento do loop principal em 87.5%.

### Comparação com Métodos Básicos
* **vs. Solução Cartesiana:** A solução cartesiana ($y = \sqrt{R^2 - x^2}$) exige uma raiz quadrada por pixel, que é uma operação pesada e resulta em "buracos" na linha quando a curvatura é acentuada. O Ponto Médio usa apenas somas e garante uma linha contínua.
* **vs. Solução Paramétrica:** A paramétrica depende de `sin` e `cos` (Séries de Taylor), que consomem muitos ciclos de CPU. O Ponto Médio ignora ângulos e trabalha apenas com a posição relativa na grade de pixels.

---

## 2. Algoritmo de Círculo de Bresenham

### Como o algoritmo decide o pixel?
Aqui temos o **Erro Acumulado**. O Bresenham não calcula a posição absoluta a cada passo; ele rastreia o quanto o pixel escolhido se desviou da curva matemática ideal.
* Ele mantém uma variável de decisão inteira ($D$). 
* A cada incremento no eixo $x$, ele verifica o sinal de $D$.
* Se o erro acumulado indica que a curva está se afastando demais do centro, ele realiza um movimento diagonal para compensar e atualiza o valor de $D$ para a próxima iteração.
* Todo o cálculo é feito de forma incremental: o erro do pixel atual é derivado do erro do pixel anterior.



### Principal Vantagem: Aritmética Inteira Pura
Este algoritmo é o "padrão ouro" para performance. Ele elimina completamente o uso de números de ponto flutuante (`float`/`double`). Ele utiliza apenas:
1. **Adição e Subtração**
2. **Bit Shifting** (deslocamento de bits para multiplicar por 2), que é a operação mais rápida que um processador pode realizar.

### Comparação com Métodos Básicos
* **vs. Solução Cartesiana:** A cartesiana requer arredondamentos (`round`) constantes para converter resultados decimais em coordenadas de pixel, o que gera imprecisão e lentidão. O Bresenham já nasce "inteiro", trabalhando nativamente com a grade do monitor.
* **vs. Solução Paramétrica:** Na paramétrica, é difícil definir o "passo" do ângulo ($\theta$). Se for pequeno demais, você processa o mesmo pixel várias vezes (redesenho inútil); se for grande, o círculo fica serrilhado ou incompleto. O Bresenham visita cada pixel da fronteira exatamente uma vez.

---

## Resumo comparativo 

| Característica | Métodos Básicos (Cartesiana/Paramétrica) | Algoritmos de Rasterização (Ponto Médio/Bresenham) |
| :--- | :--- | :--- |
| **Operações Críticas** | `sqrt`, `pow`, `sin`, `cos` | `+`, `-`, `<<` (shift) |
| **Tipo de Aritmética** | Ponto Flutuante (Lento) | Inteira (Rápido) |
| **Continuidade** | Propenso a falhas/buracos | Garante 100% de preenchimento |
| **Eficiência** | Redundante e computacionalmente caro | Otimizado via simetria e cálculos incrementais |
