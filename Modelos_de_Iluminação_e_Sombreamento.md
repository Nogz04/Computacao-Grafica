# Atividade Prática: Modelos de Iluminação e Sombreamento
**Instituição:** Universidade Franciscana (UFN)  
**Disciplina:** Computação Gráfica  
**Professor:** André Flores dos Santos  
**Data:** 11/04/2026  

---

## Parte 1 - Resumo Estruturado

### 1. Reflexão Ambiente
* **Conceito:** Trata-se de uma iluminação global que preenche o cenário uniformemente, sem possuir um ponto de origem ou direção definidos.
* **Utilidade:** É empregada para garantir que objetos situados em zonas de sombra não fiquem totalmente invisíveis, simulando o rebatimento natural da luz no ambiente.
* **Prós e Contras:** Sua grande vantagem é a simplicidade de processamento, mas a desvantagem é a perda total de profundidade e volume, resultando em uma aparência "chapada".

### 2. Reflexão Difusa
* **Conceito:** É a luz refletida por superfícies foscas que espalham a radiação de maneira igualitária para todas as direções.
* **Utilidade:** Essencial para definir o sombreamento básico e a percepção tridimensional de objetos opacos, como madeira ou tecido.
* **Prós e Contras:** Oferece um realismo sólido para formas 3D sem depender do ponto de vista do observador, mas não consegue simular o brilho de materiais polidos.

### 3. Reflexão Especular
* **Conceito:** Corresponde aos pontos de luz intensa ("highlights") que surgem em objetos lisos ou lustrosos.
* **Utilidade:** Usada para dar realismo a superfícies metálicas, plásticas ou molhadas, onde o brilho se move conforme a câmera muda de posição.
* **Prós e Contras:** Confere um aspecto sofisticado e realista ao material, porém exige cálculos mais pesados que envolvem vetores de reflexão e visão.

### 4. Modelo de Phong ($I_{f} = I_{a} + I_{d} + I_{s}$)
* **Conceito:** Uma técnica matemática que soma as componentes ambiente, difusa e especular para gerar a cor final do pixel.
* **Características:** É um sistema de iluminação local que foca na luz que atinge a superfície diretamente.
* **Exemplo Prático:** Muito comum em motores de jogos (como Unity ou Unreal) para sombrear personagens e cenários em tempo real com boa fidelidade visual.

### 5. Modelos de Sombreamento (Shading)

| Modelo | Definição Técnica | Vantagens | Desvantagens |
| :--- | :--- | :--- | :--- |
| **Flat** | Calcula a luz uma única vez para cada face plana. | Velocidade extrema de renderização. | Aspecto poligonal e pouco natural. |
| **Gouraud** | Interpola as cores calculadas nos vértices ao longo da face. | Superfícies mais suaves com baixo custo. | Pode apresentar falhas em brilhos especulares concentrados. |
| **Phong** | Interpola os vetores normais em cada ponto antes de calcular a luz. | Máximo realismo e brilhos precisos. | Alto consumo de processamento. |

---

## Parte 2 - Perguntas de Análise

**1. Por que a luz ambiente, mesmo sendo constante e sem direção, é fundamental em uma cena 3D?**
**Resposta:** Sem ela, qualquer parte do objeto que não estivesse sob incidência direta de uma lâmpada ficaria em um breu absoluto. A luz ambiente impede esse contraste irreal, permitindo que o observador reconheça as formas e detalhes mesmo nas áreas de penumbra, simulando a luz que rebate nas paredes.

**2. Qual a diferença entre uma reflexão difusa e uma reflexão especular em termos de resultado visual?**
**Resposta:** A difusa entrega um acabamento fosco e uniforme, onde a claridade muda conforme o ângulo da luz, mas não conforme a posição da câmera. A especular gera aquele "ponto de luz" brilhante característico de superfícies polidas, cujo brilho "persegue" o olhar do observador.

**3. O que muda na aparência de um objeto renderizado apenas com luz ambiente versus um com reflexão difusa e especular?**
**Resposta:** Com apenas luz ambiente, o objeto perde a tridimensionalidade e parece uma figura plana (2D) de cor única. Ao adicionar a difusa e a especular, surgem sombras, gradientes e brilhos que revelam as curvas, o volume e a textura do objeto, tornando-o palpável no espaço 3D.

**4. Em quais tipos de superfície a reflexão especular é mais evidente? Por quê?**
**Resposta:** Materiais polidos, espelhados ou metálicas (como aço inox, vidro ou lataria de carro). Isso ocorre porque esses materiais refletem os fótons quase sem absorção ou espalhamento molecular, devolvendo a luz na mesma cor da fonte original.

**5. Comparação de Shading:**

| Modelo | Realismo | Custo Computacional | Comentários |
| :--- | :--- | :--- | :--- |
| **Flat** | Baixo | Mínimo | Ideal para objetos distantes ou de baixa contagem de polígonos. |
| **Gouraud** | Médio | Moderado | Padrão equilibrado para suavizar superfícies curvas. |
| **Phong** | Alto | Elevado | Recomendado quando a precisão visual e os realces de brilho são prioritários. |

**6. O modelo de iluminação de Phong considera as interações físicas completas da luz? Se não, por que ele ainda é utilizado amplamente?**
**Resposta:** Não, ele é uma simplificação empírica (um "truque" visual) e não um cálculo físico rigoroso. Sua popularidade reside no equilíbrio perfeito entre estética e performance: ele produz imagens muito convincentes gastando apenas uma fração do poder de processamento que seria necessário para calcular a física real da luz.
