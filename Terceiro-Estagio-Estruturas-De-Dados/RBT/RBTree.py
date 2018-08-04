# coding: utf-8

print("Bem vindo...")
print(
    "........................................................................................................................................................................")

print("USO: MEDIA_CADEIRA CREDITOS\n\n\n\n")
print("DIGITE EXIT() PARA SAIR")

notas = []
credits = []

while True:
    value = input()
    if str(value) == "EXIT()":
        break

    info = value.split()
    nota = float(info[0])
    creditos = float(info[1])

    notas.append(nota)
    credits.append(creditos)

somatorio_notas = 0
somatorio_creditos = 0

for i in range(len(notas)):
    somatorio_notas += notas[i] * credits[i]
    somatorio_creditos += credits[i]

print("%.2f" % (somatorio_notas / somatorio_creditos))