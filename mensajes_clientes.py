import csv

print("💬 GENERADOR DE MENSAJES INTELIGENTE\n")

with open("clientes_interiorismo.csv", newline="") as archivo:
    reader = csv.reader(archivo)
    next(reader)

    for fila in reader:
        nombre, proyecto, presupuesto, zona, nivel = fila

        if "Alto" in nivel:
            mensaje = f"""
Hola {nombre} 👋,

Vimos tu interés en un proyecto de {proyecto} en {zona}.

Tenemos propuestas exclusivas que se ajustan a tu presupuesto de {presupuesto} y pueden elevar el diseño de tu espacio a otro nivel ✨

Podemos coordinar una reunión para mostrarte opciones personalizadas.
"""

        elif "Medio" in nivel:
            mensaje = f"""
Hola {nombre} 👋,

Gracias por tu interés en un proyecto de {proyecto} en {zona}.

Tenemos varias ideas que pueden adaptarse a tu presupuesto de {presupuesto} y lograr un excelente resultado.

¿Te gustaría que te comparta algunas propuestas?
"""

        else:
            mensaje = f"""
Hola {nombre} 👋,

Vimos tu interés en un proyecto de {proyecto}.

Podemos orientarte con algunas ideas prácticas y opciones que se ajusten a lo que buscas 😊

Quedamos atentos para ayudarte.
"""

        print("📩 MENSAJE:")
        print(mensaje)
        print("----------------------")