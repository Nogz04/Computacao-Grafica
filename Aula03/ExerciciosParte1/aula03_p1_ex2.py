import numpy as np
import matplotlib.pyplot as plt

def translacao(pontos, Tx, Ty):
    pontos_transladados = []
    for ponto in pontos:
        x_u = ponto[0] + Tx
        y_u = ponto[1] + Ty
        pontos_transladados.append((x_u, y_u))
    return pontos_transladados
    
# Dados do Slide 8
p1 = (6, 8)
p2 = (4, 5)
p3 = (8, 5)
pontos_originais = [p1, p2, p3]

Tx, Ty = 3, -4

pontos_transladados = translacao(pontos_originais, Tx, Ty)

# Fechar o triângulo para o plot
x_orig = [p[0] for p in pontos_originais] + [pontos_originais[0][0]]
y_orig = [p[1] for p in pontos_originais] + [pontos_originais[0][1]]
plt.plot(x_orig, y_orig, 'bo-', label='Pontos originais')

x_trans = [p[0] for p in pontos_transladados] + [pontos_transladados[0][0]]
y_trans = [p[1] for p in pontos_transladados] + [pontos_transladados[0][1]]
plt.plot(x_trans, y_trans, 'ro-', label='Pontos transladados')

plt.xlim(0, 15)
plt.ylim(0, 10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Translação de triângulo (Slide 8)')
plt.grid(True)
plt.legend()

print(f"Originais: {pontos_originais}")
print(f"Transladados: {pontos_transladados}")

plt.show()