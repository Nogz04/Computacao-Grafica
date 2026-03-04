import math

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

def subtrairVetores(x1, y1, z1, x2, y2, z2):
    x_subtrai = x1 - x2
    y_subtrai = y1 - y2
    z_subtrai = z1 - z2
    return x_subtrai, y_subtrai, z_subtrai

def multiplicarVetorPorEscalar(x, y, z, escalar):
    x_mult = x * escalar
    y_mult = y * escalar
    z_mult = z * escalar
    return x_mult, y_mult, z_mult

def dividirVetorPorEscalar(x, y, z, escalar):
    x_div = x / escalar
    y_div = y / escalar
    z_div = z / escalar
    return x_div, y_div, z_div

def produtoEscalar(x1, y1, z1, x2, y2, z2):
    return (x1 * x2) + (y1 * y2) + (z1 * z2)

print("Leitura das variáveis do vetor principal")

x1 = float(input("Digite o valor de X: "))
y1 = float(input("Digite o valor de Y: "))
z1 = float(input("Digite o valor de Z: "))

print("\n=== VETOR 1 ===")
print([x1, y1, z1])

while True:
    print("\n1 - Calcular tamanho do vetor")
    print("2 - Normalizar o vetor")
    print("3 - Adicionar outro vetor")
    print("4 - Subtrair outro vetor")
    print("5 - Multiplicar por um escalar")
    print("6 - Dividir por um escalar")
    print("7 - Calcular produto escalar")
    print("8 - Sair")
    
    try:
        case = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida. Tente novamente.")
        continue

    if case == 1:
        resultado = calculaTamanho(x1, y1, z1)
        print(f"\n\nA magnitude do vetor 1 é: {resultado:.2f}")

    elif case == 2:
        try:
            resultado = normalizarVetor(x1, y1, z1)
            resultadoReduzido = [f"{n:.4f}" for n in resultado]
            print(f"\n\nO vetor normalizado é: {resultadoReduzido}")
        except ZeroDivisionError:
            print("\n\nNão é possível normalizar o vetor nulo.")

    elif case == 3:
        print("\nLeitura das variáveis do novo vetor para soma")
        x2 = float(input("Digite o valor de X: "))
        y2 = float(input("Digite o valor de Y: "))
        z2 = float(input("Digite o valor de Z: "))
        resultado_soma = somarVetores(x1, y1, z1, x2, y2, z2)
        print(f"\n\nA soma dos vetores é: [{resultado_soma[0]:.2f}, {resultado_soma[1]:.2f}, {resultado_soma[2]:.2f}]")

    elif case == 4:
        print("\nLeitura das variáveis do novo vetor para subtração")
        x2 = float(input("Digite o valor de X: "))
        y2 = float(input("Digite o valor de Y: "))
        z2 = float(input("Digite o valor de Z: "))
        resultado_subtracao = subtrairVetores(x1, y1, z1, x2, y2, z2)
        print(f"\n\nA subtração resulta em: [{resultado_subtracao[0]:.2f}, {resultado_subtracao[1]:.2f}, {resultado_subtracao[2]:.2f}]")

    elif case == 5:
        escalar = float(input("\nDigite o valor do escalar: "))
        resultado_mult = multiplicarVetorPorEscalar(x1, y1, z1, escalar)
        print(f"\n\nO resultado da multiplicação é: [{resultado_mult[0]:.2f}, {resultado_mult[1]:.2f}, {resultado_mult[2]:.2f}]")

    elif case == 6:
        escalar = float(input("\nDigite o valor do escalar: "))
        if escalar == 0:
            print("\n\nNão é possível dividir por zero.")
            continue
        resultado_div = dividirVetorPorEscalar(x1, y1, z1, escalar)
        print(f"\n\nO resultado da divisão é: [{resultado_div[0]:.2f}, {resultado_div[1]:.2f}, {resultado_div[2]:.2f}]")

    elif case == 7:
        print("\nLeitura das variáveis do novo vetor para produto escalar")
        x2 = float(input("Digite o valor de X: "))
        y2 = float(input("Digite o valor de Y: "))
        z2 = float(input("Digite o valor de Z: "))
        resultado_pe = produtoEscalar(x1, y1, z1, x2, y2, z2)
        print(f"\n\nO produto escalar é: {resultado_pe:.2f}")

    elif case == 8:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")