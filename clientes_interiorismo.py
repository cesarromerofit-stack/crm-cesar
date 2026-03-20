import csv
import os

archivo_existe = os.path.isfile("clientes_interiorismo.csv")

with open("clientes_interiorismo.csv", mode="a", newline="") as archivo:
    writer = csv.writer(archivo)

    if not archivo_existe:
        writer.writerow(["Nombre", "Tipo Proyecto", "Presupuesto", "Zona", "Nivel"])

    print("🏡 Sistema de clientes - Diseño de interiores")

    nombre = input("Nombre del cliente: ")
    proyecto = input("Tipo de proyecto (sala, cocina, apartamento, oficina): ")
    presupuesto = int(input("Presupuesto estimado: "))
    zona = input("Zona: ")

    # Clasificación
    if presupuesto >= 100000:
        nivel = "🔥 Alto"
    elif presupuesto >= 50000:
        nivel = "⚡ Medio"
    else:
        nivel = "❄️ Bajo"

    writer.writerow([nombre, proyecto, presupuesto, zona, nivel])
