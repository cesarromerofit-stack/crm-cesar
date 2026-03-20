import csv

buscar = input("¿Nombre del cliente?: ")

with open("clientes_interiorismo.csv", newline="") as archivo:
    reader = csv.reader(archivo)
    next(reader)

    for fila in reader:
        nombre, proyecto, presupuesto, zona, nivel = fila

        if buscar.lower() == nombre.lower():

            if "Alto" in nivel:
                mensaje = f"""
Hola {nombre} 👋,

Vimos tu interés en un proyecto de {proyecto} en {zona}.

Tenemos propuestas exclusivas que se ajustan a tu presupuesto de {presupuesto} y pueden elevar tu espacio a otro nivel ✨

Podemos coordinar una reunión para mostrarte opciones personalizadas.
"""

            elif "Medio" in nivel:
                mensaje = f"""
Hola {nombre} 👋,

Tenemos ideas para tu proyecto de {proyecto} en {zona} que se ajustan a tu presupuesto de {presupuesto}.

¿Te gustaría ver algunas propuestas?
"""

            else:
                mensaje = f"""
Hola {nombre} 👋,

Podemos orientarte con ideas para tu proyecto de {proyecto} 😊

Quedamos atentos para ayudarte.
"""

            print("\n📩 MENSAJE:\n")
            print(mensaje)