# Respostas aos Exercícios com pergunta

## EX11)

**Pergunta:** Ao pressionar as teclas de movimento, o que acontece com os dois triângulos? Por que eles se movem em sincronia?

**Resposta:**
Ao pressionar as teclas de movimento (W, A, S, D), ambos os triângulos se deslocam simultaneamente na mesma direção. Eles se movem em sincronia porque a transformação de translação (`glTranslatef(x, y, -6)`) é aplicada à matriz de visualização logo no início da função `draw()`, logo após o `glLoadIdentity()`. 

Como essa função de translação altera o estado global da matriz de transformação antes que qualquer um dos triângulos seja desenhado, ela afeta tudo o que vem em seguida no pipeline de renderização daquele frame. Ou seja, como não há um novo `glLoadIdentity()` ou uma operação de `glPushMatrix`/`glPopMatrix` separando o desenho do primeiro triângulo do segundo, ambos herdam a mesma transformação espacial, resultando no movimento conjunto e sincronizado. 

## EX13)

**Pergunta:** O que aconteceu? Qual a diferença entre o giro dos triângulos?

**Resposta:**
Ao utilizar variáveis de rotação independentes e aplicar incrementos de valores diferentes (por exemplo, `r += 3` para o primeiro e `r2 += 2` para o segundo), os triângulos passaram a girar em velocidades distintas. O primeiro triângulo gira mais rápido que o segundo. Isso demonstra como o isolamento das matrizes (usando `glLoadIdentity()`) e o uso de variáveis de estado separadas permitem que cada objeto na cena tenha seu próprio comportamento de animação, totalmente independente do outro.

## EX14)

**Pergunta:** O que acontece consigo controlar cada triangulo sem separado agora?

**Resposta:**
Sim, agora que cada triângulo possui seu próprio conjunto de variáveis de estado (posição, rotação, escala e zoom) e as matrizes de transformação são isoladas com `glLoadIdentity()`, temos o controle total e independente sobre cada objeto da cena. Isso permite criar interações muito mais complexas, onde um objeto pode ser movido sem afetar o outro. Na prática, conseguimos tratar cada elemento como uma entidade única dentro do ambiente 3D, facilitando a criação de cenas com múltiplos componentes que se comportam de maneiras diferentes ao mesmo tempo. Agora podemos dar zoom e controlar a escala de cada triângulo de forma independente. (T1 -> WASD, ZOOM -> Scrool do mouse, T2 -> IJKL, ZOOM -> C, V)
