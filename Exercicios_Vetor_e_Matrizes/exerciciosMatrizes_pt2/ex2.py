A = [
    [2, 0, 0],
    [0, 1, 0],
    [0, 0, 7]
]

print("--- Matriz A ---")
for linha in A:
    print(linha)
print()

linhas = len(A)
colunas = len(A[0])
eh_diagonal = True

# Verifica se a matriz é quadrada e se os elementos fora da diagonal principal são zeros
if linhas != colunas:
    eh_diagonal = False
    print(f"A matriz não é quadrada ({linhas}x{colunas}).")
else:
    print(f"A matriz é quadrada ({linhas}x{colunas}). Verificando elementos...")
    for i in range(linhas):
        for j in range(colunas):
            if i != j and A[i][j] != 0:
                eh_diagonal = False
                break
                
        if not eh_diagonal:
            break

print("\n--- Resultado Final ---")
if eh_diagonal:
    print("A matriz é Diagonal.")
else:
    print("A matriz não é Diagonal.")
