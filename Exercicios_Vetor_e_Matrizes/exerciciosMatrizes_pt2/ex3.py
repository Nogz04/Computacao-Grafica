A = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print("--- Matriz A ---")
for linha in A:
    print(linha)
print()

linhas = len(A)
colunas = len(A[0])
eh_identidade = True

# Verifica se a matriz é quadrada, se a diagonal é 1 e demais elementos são 0
if linhas != colunas:
    eh_identidade = False
    print(f"A matriz não é quadrada ({linhas}x{colunas}).")
else:
    print(f"A matriz é quadrada ({linhas}x{colunas}). Verificando elementos...")
    for i in range(linhas):
        for j in range(colunas):
            if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
                eh_identidade = False
                break
                
        if not eh_identidade:
            break

print("\n--- Resultado Final ---")
if eh_identidade:
    print("A matriz é Identidade.")
else:
    print("A matriz não é Identidade.")
