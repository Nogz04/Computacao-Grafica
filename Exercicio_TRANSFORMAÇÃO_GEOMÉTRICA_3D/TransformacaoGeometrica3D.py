import numpy as np

# Definição do ponto original P -> Vetor
P = np.array([-2, 4, 1, 1])

# Matriz de Translação
Mt = np.array([
    [1, 0, 0, 5],
    [0, 1, 0, 2],
    [0, 0, 1, 3],
    [0, 0, 0, 1]
])

# Multiplicação da matriz pelo ponto P utilizando a função np.dot
P_linha = np.dot(Mt, P)

print("-" * 30)
print("EXERCÍCIO: TRANSFORMAÇÃO GEOMÉTRICA 3D")
print("-" * 30)
print("Matriz de Translação (Mt):")
print(Mt)
print("\nPonto Original (P):", P)
print("Ponto Transladado (P'):", P_linha)
print("-" * 30)