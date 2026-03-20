import csv

clientes = []

with open("clientes.csv", newline="") as archivo:
    reader = csv.reader(archivo)
    next(reader)

    for fila in reader:
        nombre, tipo, presupuesto, zona, nivel = fila
        clientes.append([nombre, tipo, int(presupuesto), zona, nivel])

# Ordenar por presupuesto (de mayor a menor)
clientes.sort(key=lambda x: x[2], reverse=True)

print("💰 CLIENTES ORDENADOS POR PRESUPUESTO:\n")

for cliente in clientes:
    print(f"Nombre: {cliente[0]}")
    print(f"Presupuesto: {cliente[2]}")
    print(f"Zona: {cliente[3]}")
    print("----------------------")