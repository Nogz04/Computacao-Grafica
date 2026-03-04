A = [
    [1, 3, 2],
    [4, 7, 6]
]

B = [
    [2, 8],
    [3, 1],
    [5, 9]
]

def imprimir_matriz(nome, matriz):
    print(f"--- Matriz {nome} ---")
    for linha in matriz:
        print(linha)
    print()

imprimir_matriz("A", A)
imprimir_matriz("B", B)

linhas_A = len(A)
colunas_A = len(A[0])
linhas_B = len(B)
colunas_B = len(B[0])

# Verifica condição de existência para multiplicação de matrizes
if colunas_A == linhas_B:
    print(f"Verificação: {colunas_A} colunas de A = {linhas_B} linhas de B. Multiplicação possível.\n")
    
    C = []
    for i in range(linhas_A):
        linha_vazia = []
        for j in range(colunas_B):
            linha_vazia.append(0)
        C.append(linha_vazia)

    # Produto de matrizes utilizando loops
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]

    imprimir_matriz("Resultado (A * B)", C)
else:
    print("Multiplicação impossível: colunas de A diferentes das linhas de B.")
