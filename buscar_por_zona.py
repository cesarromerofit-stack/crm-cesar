import csv

zona_buscar = input("¿Qué zona quieres buscar?: ")

print(f"\n📍 CLIENTES EN {zona_buscar.upper()}:\n")

with open("clientes.csv", newline="") as archivo:
    reader = csv.reader(archivo)
    next(reader)

    for fila in reader:
        nombre, tipo, presupuesto, zona, nivel = fila

        if zona_buscar.lower() in zona.lower():
            print(f"Nombre: {nombre}")
            print(f"Presupuesto: {presupuesto}")
            print(f"Nivel: {nivel}")
            print("----------------------")