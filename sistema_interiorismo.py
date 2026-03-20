import csv
import os

def agregar_cliente():
    archivo_existe = os.path.isfile("clientes_interiorismo.csv")

    with open("clientes_interiorismo.csv", mode="a", newline="") as archivo:
        writer = csv.writer(archivo)

        if not archivo_existe:
            writer.writerow(["Nombre", "Proyecto", "Presupuesto", "Zona", "Nivel"])

        print("\n➕ NUEVO CLIENTE")

        nombre = input("Nombre: ")
        proyecto = input("Proyecto: ")
        presupuesto = int(input("Presupuesto: "))
        zona = input("Zona: ")

        if presupuesto >= 100000:
            nivel = "Alto"
        elif presupuesto >= 50000:
            nivel = "Medio"
        else:
            nivel = "Bajo"

        writer.writerow([nombre, proyecto, presupuesto, zona, nivel])
        print("✅ Cliente guardado\n")


def ver_mensajes():
    print("\n💬 MENSAJES\n")

    with open("clientes_interiorismo.csv", newline="") as archivo:
        reader = csv.reader(archivo)
        next(reader)

        for fila in reader:
            nombre, proyecto, presupuesto, zona, nivel = fila

            print(f"Mensaje para {nombre}:")
            print(f"Hola {nombre}, tenemos ideas para tu {proyecto} en {zona}.")
            print("------------------")


def buscar_cliente():
    buscar = input("\n🔍 Nombre del cliente: ")

    with open("clientes_interiorismo.csv", newline="") as archivo:
        reader = csv.reader(archivo)
        next(reader)

        for fila in reader:
            nombre, proyecto, presupuesto, zona, nivel = fila

            if buscar.lower() == nombre.lower():
                print(f"\n📌 Cliente encontrado:")
                print(f"{nombre} - {proyecto} - {presupuesto} - {zona} - {nivel}")


# MENÚ PRINCIPAL
while True:
    print("""
🏡 SISTEMA DE INTERIORISMO

1. Agregar cliente
2. Ver mensajes
3. Buscar cliente
4. Salir
""")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        ver_mensajes()
    elif opcion == "3":
        buscar_cliente()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")