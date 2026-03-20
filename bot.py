import csv
import os

archivo_existe = os.path.isfile("clientes.csv")

with open("clientes.csv", mode="a", newline="") as archivo:
    writer = csv.writer(archivo)

    if not archivo_existe:
        writer.writerow(["Nombre", "Tipo", "Presupuesto", "Zona", "Nivel"])

    print("Hola 👋 Soy César Romero, asesor inmobiliario en Punta Cana")

    nombre = input("Nombre: ")
    tipo = input("¿Inversión o vivir?: ")
    presupuesto = int(input("Presupuesto: "))
    zona = input("Zona: ")

    if presupuesto >= 200000:
        nivel = "🔥 Caliente"
    elif presupuesto >= 100000:
        nivel = "⚡ Medio"
    else:
        nivel = "❄️ Frío"

    writer.writerow([nombre, tipo, presupuesto, zona, nivel])

print("Cliente guardado correctamente ✅")