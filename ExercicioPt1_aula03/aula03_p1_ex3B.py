import matplotlib.pyplot as plt

def escala(pontos, Sx, Sy):
    pontos_escala = []
    for ponto in pontos:
        x_u = ponto[0] * Sx
        y_u = ponto[1] * Sy
        pontos_escala.append((x_u, y_u))
    return pontos_escala

# Exercício 03 b
p1 = (2, 2)
p2 = (4, 4)
Sx, Sy = 2, 2

pontos_escala = escala([p1, p2], Sx, Sy)

print("Pontos escalados:")
for ponto in pontos_escala:
    print(ponto)

plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'bo-', label='Pontos originais')

p1_esc, p2_esc = pontos_escala[0], pontos_escala[1]
lista_x = [p1_esc[0], p2_esc[0]]
lista_y = [p1_esc[1], p2_esc[1]]

plt.plot(lista_x, lista_y, 'ro-', label='Pontos escalados')

plt.xlim(-7, 10) 
plt.ylim(-7, 10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Escala de pontos no plano cartesiano (Exercicio 03 b)')
plt.grid(True)
plt.legend()

plt.show()
