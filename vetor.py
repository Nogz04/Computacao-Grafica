import math

# Função que calcula o tamanho ou magnitude de um vetor
def calculaTamanho(x, y, z):
    tam = math.sqrt(x*x + y*y + z*z)
    return tam

def normalizarVetor(x,y,z):
    tam = calculaTamanho(x,y,z)
    x = x/tam
    y = y/tam
    z = z/tam
    return x,y,z

def somarVetores(x1, y1, z1, x2, y2, z2):
    x_soma = x1 + x2
    y_soma = y1 + y2
    z_soma = z1 + z2
    return x_soma, y_soma, z_soma

def subtrairPrimeiroVetorPeloSegundo(x1, y1, z1, x2, y2, z2):
    x_subtrai = x1 - x2
    y_subtrai = y1 - y2
    z_subtrai = z1 - z2
    return x_subtrai, y_subtrai, z_subtrai

def subtrairSegundoVetorPeloPrimeiro(x1, y1, z1, x2, y2, z2):
    x_subtrai = x2 - x1
    y_subtrai = y2 - y1
    z_subtrai = z2 - z1
    return x_subtrai, y_subtrai, z_subtrai

print("Leitura das variáveis do primeiro vetor")

x1 = float(input("Digite o valor de X: "))
y1 = float(input("Digite o valor de Y: "))
z1 = float(input("Digite o valor de Z: "))

print("\n=== VETOR 1 ===")
print([x1, y1, z1])

print("\nLeitura das variáveis do segundo vetor")
x2 = float(input("Digite o valor de X: "))
y2 = float(input("Digite o valor de Y: "))
z2 = float(input("Digite o valor de Z: "))

print("\n=== VETOR 2 ===")
print([x2, y2, z2])

while True:
    print("\n1 - Calcular tamanho do primeiro vetor")
    print("2 - Normalizar o primeiro vetor")
    print("3 - Somar os dois vetores")
    print("4 - Subtrair o vetor 1 do 2")
    print("4 - Subtrair o vetor 2 do 1")
    print("5 - Sair")
    

    if case := int(input("Digite a opção desejada: ")):
        if case == 1:
            resultado = calculaTamanho(x1, y1, z1)
            print(f"\n\nA magnitude do vetor 1 é: {resultado:.2f}")

        elif case == 2:
            resultado = normalizarVetor(x1, y1, z1)
            resultadoReduzido = [f"{n:.4f}" for n in resultado]
            print(f"\n\nO vetor 1 normalizado é: {resultadoReduzido}")

        elif case == 3:
            resultado_soma = somarVetores(x1, y1, z1, x2, y2, z2)
            print(f"\n\nA soma dos vetores é: [{resultado_soma[0]:.2f}, {resultado_soma[1]:.2f}, {resultado_soma[2]:.2f}]")

        elif case == 4:
            resultado_subtracao = subtrairPrimeiroVetorPeloSegundo(x1, y1, z1, x2, y2, z2)
            print(f"\n\nA subtração do primeiro vetor pelo segundo é: [{resultado_subtracao[0]:.2f}, {resultado_subtracao[1]:.2f}, {resultado_subtracao[2]:.2f}]")

        elif case == 5:
            resultado_subtracao = subtrairSegundoVetorPeloPrimeiro(x1, y1, z1, x2, y2, z2)
            print(f"\n\nA subtração do segundo vetor pelo primeiro é: [{resultado_subtracao[0]:.2f}, {resultado_subtracao[1]:.2f}, {resultado_subtracao[2]:.2f}]")

        elif case == 6:
            print("Saindo do programa...")
            break


        else:
            print("Opção inválida. Tente novamente.")