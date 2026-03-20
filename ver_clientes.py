import csv

print("🔥 CLIENTES CALIENTES:\n")

with open("clientes.csv", newline="") as archivo:
    reader = csv.reader(archivo)

    next(reader)  # saltar encabezados

    for fila in reader:
        nombre, tipo, presupuesto, zona, nivel = fila

        if "Caliente" in nivel:
            print(f"Nombre: {nombre}")
            print(f"Presupuesto: {presupuesto}")
            print(f"Zona: {zona}")
            print("----------------------")