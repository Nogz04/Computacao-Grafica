A = [
    [2, 3, 8],
    [6, 0, 4],
    [1, 5, 7]
]

print("--- Matriz A (Original) ---")
for linha in A:
    print(linha)
print()

linhas = len(A)
colunas = len(A[0])

# Inicializa a matriz transposta adequando as dimensões
transposta = []
for i in range(colunas):
    linha_vazia = []
    for j in range(linhas):
        linha_vazia.append(0)
    transposta.append(linha_vazia)

# Transpõe os elementos trocando linhas por colunas
for i in range(linhas):
    for j in range(colunas):
        transposta[j][i] = A[i][j]

print("--- Matriz Transposta (A^T) ---")
for linha in transposta:
    print(linha)
