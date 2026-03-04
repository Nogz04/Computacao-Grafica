A = [
    [2, 3, 8],
    [6, 0, 4],
    [1, 5, 7]
]

escalar = 3

linhas = len(A)
colunas = len(A[0])

resultado = []
for i in range(linhas):
    linha_vazia = []
    for j in range(colunas):
        linha_vazia.append(0)
    resultado.append(linha_vazia)

# Obtém o múltiplo escalar multiplicando cada elemento da matriz
for i in range(linhas):
    for j in range(colunas):
        resultado[i][j] = A[i][j] * escalar

print("--- Matriz Original A ---")
for linha in A:
    print(linha)

print(f"\n--- Matriz Resultante ({escalar} * A) ---")
for linha in resultado:
    print(linha)
